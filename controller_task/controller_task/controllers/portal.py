from odoo.http import request
from odoo import http
import base64

class Products(http.Controller):

    @http.route('/products', type='http', auth="public", website=True)
    def products(self,**kw):
        products=request.env['product.product'].search([])
        return request.render('controller_task.product_page', {'products':products})

    # @http.route('/products<model("product.product"):product>', type='http', auth="public", website=True)
    # def product_details(self,product):
    #     return request.render('product.product_normal_form_view', {'product':product})    

class Partners(http.Controller):
    @http.route('/partners',type='http', auth="public", website=True) 
    def partner(self,**kw):
        return request.render('controller_task.partner_page',{})

    @http.route('/create_patient',type='http', auth="public", website=True) 
    def createpartner(self,**kw):
        print("Submit Button clicked---------------------------------",kw)
        file = kw.get('image_1920')
        filename=base64.b64encode(file.read())
        print('-------------',filename)
        vals={
        'name':kw.get('name'),
        'phone':kw.get('phone'),
        'email':kw.get('email'),
        'image_1920':filename
        }
        partner=request.env['res.partner'].create(vals)

        Attachment = request.env['ir.attachment']
        file_name = kw.get('image_1920').filename
        # file = post.get('attachment')
        attachment_id = Attachment.create({
        'name': file_name,
        'type': 'binary',
        'datas': filename,
        'res_model': partner._name,
        'res_id': partner.id
        })


        return request.render('website.contactus_thanks',{}) 

class Custom(http.Controller):
    @http.route('/mypage',type='http', auth="public", website=True) 
    def myfunc(self,**kw):
        return request.render('controller_task.my_page',{})              