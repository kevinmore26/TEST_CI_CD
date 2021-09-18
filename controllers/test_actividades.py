from app import app
from unittest import TestCase

class TestActividadesController(TestCase):
    def setUp(self):
        '''Es el método oque servirá para configrar mis test de esta clase'''
        self.app = app.test_client()
        # para que el servidor piense que el servidor se levantó, pero no es así
    
    def test_get_actividades(self):
        respuesta = self.app.get('/actividades')
        print(respuesta.json)
        self.assertEqual(respuesta.json, dict(message=None,content=[{
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
            }]))

        self.assertEqual(respuesta.status_code,201)
