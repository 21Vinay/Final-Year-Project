from flask import Flask , render_template , request
app = Flask (__name__)

ips  = []
port = []

@app.before_request
def getIP():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        x = request.environ['REMOTE_ADDR']


    else:
        x = request.environ['HTTP_X_FORWARDED_FOR']
    por = request.environ['REMOTE_PORT']
    ips.append(x)
    port.append(por)
    dist = {'ips': ips, 'port': port}
    return render_template("ddos.html", dist=dist)

@app.route('/')
def hello_world():
    # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    #     x = request.environ['REMOTE_ADDR']
    #
    # else:
    #     x = request.environ['HTTP_X_FORWARDED_FOR']
    # port  = request.environ['REMOTE_PORT']
    dist = {'ips':ips , 'port':port}
    return render_template("ddos.html" , dist = dist )



if __name__ == '__main__':

    app.run(debug=False , host='0.0.0.0')
