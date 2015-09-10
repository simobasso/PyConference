from pycon.core.views import PyconTemplateView
from pycon.sponsors.models import Sponsor


class VenueView(PyconTemplateView):
    template_name = 'venue/venue.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'location': "123 Benton Road",
            'sponsors': Sponsor.objects.all().order_by('level'),
        })
