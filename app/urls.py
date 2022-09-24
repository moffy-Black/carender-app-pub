from app.controllers import api, IndexController, LoginController, InsertController, MatchController, DuplicateController, DetailController, DeleteContoroller

api.add_route('/index', IndexController)
api.add_route('/', LoginController)
api.add_route('/insert', InsertController)
api.add_route('/match', MatchController)
api.add_route('/duplicate', DuplicateController)
api.add_route('/detail/{name}', DetailController)
api.add_route('/delete/{name}/{time}', DeleteContoroller)