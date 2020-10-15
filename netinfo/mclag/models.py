from django.db import models

NAPALM_MAPPING = {
    'iosxr': 'iosxr'
}


class Host(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=70)
    port = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    Platform = models.CharField(max_length=30, choices=(("iosxr", "CISCO IOSXR"), ("iosxe", "CISCO IOSXE"), ("ios", "CISCO IOS")), blank=True)

    def __str__(self) -> str:
        return self.name


    @property
    def napalm_driver(self)->str:
        return NAPALM_MAPPING[self.Platform]
            