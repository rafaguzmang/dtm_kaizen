from odoo import models,fields,api
from datetime import datetime

class Kaizen(models.Model):
    _name = "dtm.kaizen"
    _description = "Modelo para llevar el listado de las actividades"

    actividades = fields.Text(string="Actividad")
    departamento_id = fields.Many2one("dtm.kaizen.departamento", string="Área o Departamento")
    fecha_inicio = fields.Date(string="Fecha de inicio",default=datetime.today())
    fecha_compromiso = fields.Date(string="Fecha de Compromiso",default=datetime.today())
    indicador_impacta = fields.Char(string="Indicador que Impacta")
    fecha_cierre = fields.Date(string="Feche cierre real",default = datetime.today())
    responsable_id = fields.Many2one("dtm.kaizen.responsable",string="Responsable")
    objetivo = fields.Text(string="Objetivo")
    nivel_accion = fields.Selection(string="Nivel de acción",selection=[("inmediata","Inmediata"),
                                         ("correctiva","Correctiva"),("preventiva","Preventiva")])
    status = fields.Text(string="Estatus")
    comentarios = fields.Text(string="Comentarios")
    notas = fields.Text(string="Notas")
    evidencia = fields.Binary()

    cronometro = fields.Integer()

    def get_view(self, view_id=None, view_type='form', **options):
        res = super(Kaizen,self).get_view(view_id, view_type,**options)
        get_rows = self.env['dtm.kaizen'].search([])

        for row in get_rows:
            print(datetime.today(),datetime.today().strftime("%j"))
            cronometro = int(row.fecha_compromiso.strftime("%j"))-int(datetime.today().strftime("%j"))
            row.write({"cronometro":cronometro})
        return  res


class Departamento(models.Model):
    _name = "dtm.kaizen.departamento"
    _description = "Modelo para guardar el nombre de los diferentes departamentos"
    _rec_name = "nombre"

    nombre = fields.Char(string="Área/Departamento")

class Responsable(models.Model):
    _name = "dtm.kaizen.responsable"
    _description = "Modelo para guardar el nombre del personal responsable"
    _rec_name = "nombre"

    nombre = fields.Char(string="Responsable")
