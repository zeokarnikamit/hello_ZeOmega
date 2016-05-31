# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from flask import Flask, render_template

app = Flask(__name__)


def strong_deco(func):
    def strong_wrapper(name):
        return '<b>{0}</b>'.format(func(name))
    return strong_wrapper


def p_deco(func):
    def p_wrapper(name):
        return '<p>{0}</p>'.format(func(name))
    return p_wrapper


def div_deco(func):
    def div_wrapper(name):
        return '<div>{0}</div>'.format(func(name))
    return div_wrapper


@app.route('/greet/<name>')
@div_deco
@p_deco
@strong_deco
def greet(name):
    return render_template('deco.html', text='Hello {0}'.format(name))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
