from flask_restplus import Resource, Namespace, reqparse, fields

api = Namespace('cats', description='cat related operations')

parser = reqparse.RequestParser()

cat = api.model('cat_model', {
    'id': fields.String(required=True, description='Cat Id'),
    'name': fields.String(required=True, description='Cat Name')
})

cats_list = [{
    'id': 'first',
    'name': 'first_cat'
}]


@api.route('/')
class CatList(Resource):
    @api.marshal_list_with(cat)
    def get(self):
        return cats_list


@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat with specified id not found')
class EachCat(Resource):
    @api.marshal_with(cat)
    def get(self, id):
        for cat in cats_list:
            if cat['id'] == id:
                return cat
        api.abort(404)


@api.route('/add_cat')
@api.response(404, 'insertion failed')
class InsertCat(Resource):

    @api.marshal_with(cat)
    def post(self):
        parser.add_argument('id', location='form')
        parser.add_argument('name', location='form')
        args = parser.parse_args()

        for cat in cats_list:
            if cat['id'] == args['id']:
                raise Exception

        cats_list.append({
                    'id': args['id'],
                    'name': args['name']
                 })

        return cats_list
