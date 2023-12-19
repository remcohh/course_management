{
    'name': "Course management",
    'summary': '',
    'author': "Remco Huijdts",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'depends': ['base', 'product', 'sale', 'website_sale_stock'],
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
        "views/product_template.xml",
        "views/product_stage.xml",
        "views/grading_profile.xml",
        "views/web_templates.xml"
    ],

    'assets': {
        'web.assets_frontend': [
            'course_management/static/src/xml/**/*',
            'course_management/static/src/js/**/*',

        ]
    }
}
