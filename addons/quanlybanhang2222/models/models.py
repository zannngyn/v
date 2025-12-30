# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hang(models.Model):
    _name = 'hang'
    _description = "Hàng Hóa"

    tenhang = fields.Char(string="Tên Hàng", required=True)
    mahang = fields.Integer(string="Mã Hàng", required=True)
    diachi = fields.Char(string="Địa Chỉ", required=True)
    sodt = fields.Char(string="Số Điện Thoại", required=True)


class nhanvien(models.Model):
    _name = 'nhanvien'
    _description = "Nhân Viên"

    tennv = fields.Char(string="Tên Nhân Viên", required=True)
    manv = fields.Integer(string="Mã Nhân Viên", required=True)
    gioitinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string="Giới Tính", required=True)
    sodt = fields.Char(string="Số Điện Thoại", required=True)


class sanpham(models.Model):
    _name = 'sanpham'
    _description = "Sản Phẩm"

    masp = fields.Char(string="Mã Sản Phẩm", required=True)
    tensp = fields.Char(string="Tên Sản Phẩm", required=True)
    soluong = fields.Integer(string="Số Lượng", required=True)
    giaban = fields.Integer(string="Giá", required=True)
    mausac = fields.Selection([('do', 'Đỏ'), ('xanh', 'Xanh'), ('vang', 'Vàng')], string="Màu Sắc", required=True)