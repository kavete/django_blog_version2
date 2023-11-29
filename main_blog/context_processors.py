from main_blog.forms import SubscriberForm
from main_blog.models import Tag


def get_all_tags(request):
    all_tags = Tag.objects.all().order_by("?")[:10]
    return {"all_tags": all_tags}


def subscription_form(request):
    form = SubscriberForm()
    return {'subscription_form': form}
