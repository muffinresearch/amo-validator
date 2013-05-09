import logging

from celeryutils import task

from amo.decorators import write


log = logging.getLogger('z.task')


@task
@write
def update_supported_locales_single(id, latest=False, **kw):
    """
    Update supported_locales for an individual app. Set latest=True to use the
    latest current version instead of the most recent public version.
    """
    from mkt.webapps.models import Webapp

    app = Webapp.objects.get(pk=id)
    try:
        if app.update_supported_locales(latest=latest):
            log.info(u'[Webapp:%s] Updated supported locales' % app.id)
    except Exception:
        log.info(u'[Webapp%s] Updating supported locales failed.' % app.id,
                 exc_info=True)