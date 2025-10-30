from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape
import controler as ctl

def _esc(v):
    return escape("" if v is None else str(v))

comTrole = ctl.Controler()


class LivroController(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(302)
            self.send_header("Location", "/menu")
            self.end_headers()

        elif self.path == "/menu":
            with open("View_and_Interface/menu.html", "rb") as f:
                conteudo = f.read()
            self._send_html(conteudo)

        elif self.path == "/cadastrar_livro":
            with open("View_and_Interface/cadastrar_livro.html", "rb") as f:
                conteudo = f.read()
            self._send_html(conteudo)

        elif self.path == "/listar_livros":
            livros = comTrole.Get_Livros()
            resposta = ""
            for livro in livros:
                autores = ", ".join(livro.autores)
                resposta += f"""
                <div class='item'>
                    <p><b>Título:</b> {_esc(livro.titulo)}</p>
                    <p><b>Autores:</b> {_esc(autores)}</p>
                    <p><b>ISBN:</b> {_esc(livro.ISBN)}</p>
                    <p><b>Ano:</b> {_esc(livro.ano)}</p>
                    <p><b>Cópias:</b> {_esc(livro.copiasDisponiveis)}/{_esc(livro.copiasTotal)}</p>
                    <p><b>Status:</b> {_esc(livro.status)}</p>
                    <form method="POST" action="/remover_livro">
                        <input type="hidden" name="isbn" value="{_esc(livro.ISBN)}">
                        <button type="submit">Remover</button>
                    </form>
                </div>
                <hr>
                """

            with open("View_and_Interface/listar_livros.html", "r", encoding="utf-8") as f:
                conteudo = f.read()
            conteudo = conteudo.replace("<!--LIVROS-->", resposta)
            self._send_html(conteudo.encode("utf-8"))

    def do_POST(self):
        if self.path == "/cadastrar":
            tamanho = int(self.headers["Content-Length"])
            dados = self.rfile.read(tamanho).decode("utf-8")
            params = parse_qs(dados)

            dados_livro = {
                "titulo": params.get("titulo", [""])[0],
                "autores": [a.strip() for a in params.get("autores", [""])[0].split(",")],
                "isbn": params.get("isbn", [""])[0],
                "ano": params.get("ano", [""])[0],
                "copiasTotal": params.get("copiasTotal", [""])[0],
                "copiasDisponiveis": params.get("copiasDisponiveis", [""])[0],
            }

            comTrole.Ctr_Adicionar_Livro(dados_livro)

            with open("View_and_Interface/livro_cadastrado.html", "r", encoding="utf-8") as f:
                conteudo = f.read()

            conteudo = conteudo.replace("<!--TITULO-->", _esc(dados_livro["titulo"]))
            conteudo = conteudo.replace("<!--ISBN-->", _esc(dados_livro["isbn"]))
            self._send_html(conteudo.encode("utf-8"))

        elif self.path == "/remover_livro":
            tamanho = int(self.headers["Content-Length"])
            dados = self.rfile.read(tamanho).decode("utf-8")
            params = parse_qs(dados)
            isbn = params.get("isbn", [""])[0]

            comTrole.Remover_Livro(isbn)

            self.send_response(302)
            self.send_header("Location", "/listar_livros")
            self.end_headers()

    def _send_html(self, conteudo):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(conteudo)


if __name__ == "__main__":
    servidor = HTTPServer(("localhost", 8080), LivroController)
    print("Servidor rodando em http://localhost:8080")
    servidor.serve_forever()
