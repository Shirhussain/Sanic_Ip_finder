
import ipapi

from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic(name='Sanic Web Tutorial')
jinja = SanicJinja2(app, pkg_name="main")


@app.route("/", methods =['GET', 'POST'])
async def index(request):
    search = request.form.get("search")
    data = ipapi.location(ip=search, output='json')

    return jinja.render("index.html", request, data=data)




if __name__=="__main__":
    app.run(host ="127.0.0.1",port=8001, debug=True)
