from django.dispatch import Signal

result_received = Signal(providing_args=["InvId", "OutSum"])
success_page_visited = Signal(providing_args=["InvId", "OutSum"])
fail_page_visited = Signal(providing_args=["InvId", "OutSum"])


# yandex money

# from django.dispatch import Signal

# payment_process = Signal()
# payment_completed = Signal()

