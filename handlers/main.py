#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = self.request.get("kilometros", "0")
        minutos = self.request.get("minutos", "0")
        consumoMedio = self.request.get("consumoMedio", "0")

        if len(kilometros.strip()) == 0:
            try: 
                float(kilometros) 
            except:
                kilometros = 0

        if( len(minutos.strip()) == 0):
            try: 
                float(minutos) 
            except:
                minutos = 0  

        if len(consumoMedio.strip()) == 0:
            try: 
                float(consumoMedio) 
            except:
                consumoMedio = 0 

        if kilometros != 0 and  minutos != 0 and consumoMedio != 0:
            horas = minutos / 60
            consumoTotal = consumoMedio * kilometros
            velocidadMedia = kilometros / horas

        self.response.write('Velocidad media: ' + str(velocidadMedia) + ' km/h' + '\nConsumo total: ' + str(consumoTotal) + ' l/km')

app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
