from django.shortcuts import render, HttpResponse
import json

times = 0


def resetPassword(request):
    global times
    print('Reset Password Page Opened!')
    times += 1
    if request.path == '/reset-password/':
        report_loc = '/dashboard/'
    else:
        report_loc = '/reset-password/'
    return render(request, 'reset-password.html', {'loc': report_loc, 'error': ''})


def resetPasswordAction(request):
    print('Reset Password Request Made!')
    print('Reading Data from JSON')
    json2 = open('user_data.json',)
    data = json.load(json2)
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close()
    print('Read data from JSON')
    global times
    times = times+1
    if request.path == '/reset-password/':
        report_loc = '/dashboard/'
    else:
        report_loc = '/login/'
    email = request.POST['email']
    oldPassword = request.POST['old_password']
    newPassword = request.POST['new_password']
    new_password1 = request.POST['new_password1']
    if new_password1 == newPassword:
        if newPassword == oldPassword:
            print('Old and new passwords are same, returning HTTP response')
            return render(request, 'reset-password.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. Old and new passwords cannot be same.'})
        if email in emails:
            print('email index: ', emails.index(email))
            if passwords[emails.index(email)] == oldPassword:
                d4 = {emails[len(emails)-1]: newPassword}
                for x in range(len(emails)-1):
                    d4 = dict(list(d4.items()) +
                                list({emails[x]: passwords[x]}.items()))
                json_object = '{"u_data": ['+json.dumps(d4, indent=4)+']}'
                a = open('user_data.json', 'w')
                a.write(json_object)
                a.close()
                times = 0
                print('Password reset for user, returning HTTP response')
                return HttpResponse('Your password reset successfully')
        elif email not in emails:
            print('Account does not exist, returning HTTP response')
            return render(request, 'reset-password.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. No such account exists. Consider signing up!'})
    else:
        print('Passwords do not match, returning HTTP response')
        return render(request, 'reset-password.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. The Passwords do not match.'})
