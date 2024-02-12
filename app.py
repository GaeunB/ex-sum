# -*- coding: utf-8 -*-
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
from ext import textrank_summarize

app = Flask(__name__)

cors = CORS(app)

@app.route('/')	
def index():
	return render_template('index.html')

#요약하기 후 몇 초 기다려야함.
@app.route('/key',methods=['POST'])
def key():
	try:
		data = request.get_json(force=True)
		context = data['context']
		keytext = textrank_summarize(context,2)
		response = jsonify({'keytext': keytext})

	except Exception as e:
		response = jsonify({'error': str(e)})	
		
	return response
	

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=5000,debug=True)