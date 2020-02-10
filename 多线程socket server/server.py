#-*-coding:utf-8-*-
# Author:Lu Wei
# import socketserver
#
# class MYSERVER(socketserver.BaseRequestHandler):
#     def handle(self):
#         while True:
#             msg=self.request.recv(1024).decode('utf-8')
#             self.request.send(msg.upper().encode('utf-8'))
# server=socketserver.ThreadingTCPServer(('127.0.0.1',9000),MYSERVER)
# server.serve_forever()