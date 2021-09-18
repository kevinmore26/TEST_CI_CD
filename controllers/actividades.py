from flask_restful import Resource, reqparse

class ActividadesController(Resource):
    def get(self):
        return{
            "message":None,
            "content":[{
                "actividadId":1,
                "actividadNombre":"ir a la playa"
            },
                {
                "actividadId":2,
                "actividadNombre":"ir a comer"
            },
            {
                "actividadId":3,
                "actividadNombre":"ir al cumple de mi abuela"
            }]
        },201