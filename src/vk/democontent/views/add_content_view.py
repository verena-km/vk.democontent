# -*- coding: utf-8 -*-

# from vk.democontent import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAddContentView(Interface):
    """Marker Interface for IAddContentView"""


@implementer(IAddContentView)
class AddContentView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('add_content_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
