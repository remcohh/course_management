# -*- coding: utf-8 -*-
{
    'name': "Course management",
    'summary': '',
    'author': "Remco",
    'category': 'Uncategorized',
    'version': '0.1',
    'application':True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],
    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/registration.xml",
        "views/student.xml",
        "views/edition.xml",
        "views/session.xml",
        "views/attendance.xml",
        "views/grade.xml",
        "views/test.xml",
        "views/teacher.xml",
        "views/skill.xml",
        "views/location.xml",
    ],
}