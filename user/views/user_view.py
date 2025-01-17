from flask import render_template, request, redirect, url_for, session
from user.controllers import user_controller, test_controller


def list_users_view():
    users = user_controller.get_all_users()
    return render_template("user/users.html", users=users)


def create_user_view():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        user_controller.create_user(first_name, last_name, email, phone, password)
        return redirect(url_for("user_bp.users"))
    return render_template("user/create_user_form.html")


def login_user_view():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        message = user_controller.perform_login(email, password)
        if message == "login success":
            return redirect(url_for("user_bp.dashboard"))
            # return render_template('user/dashboard.html')
        else:
            alert_message = "Incorrect username or password. Pease try again."
            return render_template("user/login_form.html", alert_message=alert_message)
    else:
        if session.get("logged_in") is not None:
            # return render_template('user/dashboard.html')
            return redirect(url_for("user_bp.dashboard"))
        else:
            return render_template("user/login_form.html")


def user_dashboard_view():
    if session.get("logged_in") is not None:
        all_tests = test_controller.get_all_tests()
        return render_template("user/dashboard.html", all_tests=all_tests)
    else:
        return redirect(url_for("user_bp.login"))


def user_aarp_tests_view():
    if session.get("logged_in") is not None:
        aarp_tests = test_controller.get_aarp_tests()
        test_cases = test_controller.get_all_test_cases()
        test_suits = test_controller.get_all_test_suites()
        return render_template("user/aarp.html", aarp_tests=aarp_tests, test_cases=test_cases, test_suits =test_suits)
    else:
        return redirect(url_for("user_bp.login"))


def user_inogen_tests_view():
    if session.get("logged_in") is not None:
        return render_template("user/inogen.html")
    else:
        return redirect(url_for("user_bp.login"))


def user_rif_tests_view():
    if session.get("logged_in") is not None:
        return render_template("user/rif.html")
    else:
        return redirect(url_for("user_bp.login"))


def user_jaya_tests_view():
    if session.get("logged_in") is not None:
        return render_template("user/jaya.html")
    else:
        return redirect(url_for("user_bp.login"))


def user_greeting_genie_tests_view():
    if session.get("logged_in") is not None:
        return render_template("user/greeting_genie.html")
    else:
        return redirect(url_for("user_bp.login"))

def user_reports_view():
    if session.get("logged_in") is not None:
        all_tests_dashboard = test_controller.get_tests_for_dashboard()
        return render_template("user/reports.html", all_tests_dashboard=all_tests_dashboard)
    else:
        return redirect(url_for("user_bp.login"))
    
def user_charts_view():
    if session.get("logged_in") is not None:
        return render_template("user/charts.html")
    else:
        return redirect(url_for("user_bp.login"))
        
def display_aarp_test_view(template, test_name, test_title, test_data):
    if session.get("logged_in") is not None:
        return render_template(
            "user/aarp/" + template + ".html",
            test_name=test_name,
            test_title=test_title,
            test_data = test_data,
        )
    else:
        return redirect(url_for("user_bp.login"))
