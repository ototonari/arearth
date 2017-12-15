# 標準モジュールをimportする
import cgi
import os
import time

class Request(object):
    """
    HTTPのリクエストをハンドリングするクラス
    CGI側でインスタンを生成することによって利用する
    クエリデータや環境変数へのアクセス、主要ヘッダへの
    アクセス用メソッドを提供
    """
    def __init__(self, environ=os.environ):
        """
        インタンス初期化メソッド
        クエリ、環境変数をアトリビュートとして保持する
        """
        self.form=cgi.FieldStorage()
        self.environ=environ

class Response(object):
    """
    HTTPのレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成して利用する
    レスポンスやヘッダの内容の保持、ヘッダを含めたレスポンスの送信を行う
    """
    def __init__(self):
        """
        インスタンス用の初期化メソッド
        ヘッダ用の辞書、本文用の文字列などを初期化する

        """
        self.http_headers={'contenttype': 'Content-Type: text/html;'}
        self.html=""
        self.body=""
        self.head=""

    def set_http_header(self, name, value):
        """
         レスポンスのヘッダを設定する
        :param name:
        :param value:
        :return:
        """
        self.http_headers[name]=value

    def get_http_header(self, name):
        """
        設定済みのレスポンス用ヘッダを返す
        :param name:
        :return:
        """
        return self.http_headers.get(name, None)

    def set_html(self):
        """
        レスポンスとして出力する本文の文字列を返す
        :param bodystr:
        :return:
        """
        htmlstr = get_htmltemplate()
        self.html=htmlstr.format(head=self.head, body=self.body)
    
    def get_html(self):
        return self.html

    def set_header(self, headers):
        tag = ""
        if headers:
            for line in headers:
                tag += "<{}>\n".format(line)
        self.head = tag

    def get_header(self):
        return self.head

    def set_body(self, bodystr):
        self.body = bodystr

    #import html file
    def import_html(self, path):
        try:
            html = ""
            with open(path, mode='r', encoding = 'utf-8') as htmlstr:
                for line in htmlstr:
                    html += line
            res = self.get_http_header('contenttype')
            res += '\n\n'
            res += html
            return res

        except:
            raise ValueError('import_html error')

    def make_output(self):
        """
        ヘッダと本文を含めたレスポンス文字列を作る
        :param timestamp:
        :return:
        """
        res = self.get_http_header('contenttype')
        res += '\n\n'
        res += self.html
        return res

    def redirect_to(self, url):
        """
        urlを受け取り、リダイレクトのレスポンスを送信する
        """
        res = self.get_http_header('contenttype')
        res += '\n\n'
        res += '<meta http-equiv="refresh" content="0;URL={}">'.format(url)
        print(res)



def get_htmltemplate():
    """
    レスポンスとして返すHTMLのうち、提携部分を返す
    :return:
    """
    html_body = """
<html>
        <head>
            <meta http-equiv="content-type"
                content="text/html;charset=utf-8" />
            {head}
        </head>
        <body>
        {body}
        </body>
</html>"""
    return html_body

def get_script():
    script = """
<script>alert("わーい");</script>
"""
    return script