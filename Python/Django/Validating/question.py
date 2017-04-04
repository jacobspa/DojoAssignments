def questions(request):
    is_valid = True
    if request.form['html_1'] < 18:
        messages.error(request, 'Must be 18 or older to Register for Validating.com')
        is_valid = False
    age = request.form['html_age']
    gender = request.form['html_gender']
    height = request.form['html_height']
    language = request.form['html_language']
    stack = request.form['html_stack']
    religion = request.form['html_religion']
    zipcode = request.form['html_zip']
    smoke = request.form['html_smoke']
    body = request.form['html_body']
    ethnicity  = request.form['html_ethnicity']
    children = request.form['html_children']

    Question.objects.create(age=age, gender=gender, height=height, langauge=language, stack=stack, religion=religion, zipcode=zipcode, smoke=smoke, body=body, ethnicity=ethnicity, children=children)

    return redirect('dating:home')

def viewUser(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
        'Photo':User.objects.get(id=user_id__photo)

    }
    return render(request, 'validating_app/view.html')
