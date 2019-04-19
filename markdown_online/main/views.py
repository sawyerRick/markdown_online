from django.shortcuts import render, redirect
from django.http import JsonResponse

import markdown

# Create your views here.

def main(request):
	if request.method == "GET":

		return render(request, 'markdown_online/main.html')

	if request.method == "POST":
		content = request.POST.get("content", None)
		content = markdown.markdown(content, extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			# 目录扩展
			'markdown.extensions.toc',
		])
		print(content)

		return render(request, 'markdown_online/main.html', {"content": content})