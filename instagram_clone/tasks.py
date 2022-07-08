from celery import shared_task

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return 10


@shared_task
def rename_widget(widget_id, name):
    print("ya borre todo")