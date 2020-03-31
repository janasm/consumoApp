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
        km = 0
        mn = 0
        cMedio = 0

        if len(kilometros.strip()) == 0:
            try:
                km = float(kilometros)
            except:
                self.response.write('El campo kilómetros debe tener un valor numérico.')

        if len(minutos.strip()) == 0:
            try:
                mn = int(minutos)
            except:
                self.response.write('El campo minutos debe tener un valor numérico.')

        if len(consumoMedio.strip()) == 0:
            try:
                cMedio = float(consumoMedio)
            except:
                self.response.write('El campo consumo medio debe tener un valor numérico.')

        if km != 0 and mn != 0 and cMedio != 0:
            horas = mn / 60
            consumoTotal = cMedio * km
            velocidadMedia = km / horas

        self.response.write(
            'Velocidad media: ' + str(velocidadMedia) + ' km/h' + '\nConsumo total: ' + str(consumoTotal) + ' l/km')


app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
