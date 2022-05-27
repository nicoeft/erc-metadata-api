from django.db import models

CATEGORY_CHOICES = ((0, "ERC721"), (1, "ERC1155"))


class SmartContract(models.Model):
    address = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    decimals = models.IntegerField(default=0)
    abi = models.JSONField(blank=True, null=True)


class Metadata(models.Model):
    token_id = models.IntegerField()
    smart_contract = models.ForeignKey(
        SmartContract, on_delete=models.CASCADE, related_name="metadata"
    )
    name = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255, blank=True, null=True)
    animation_url = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=None, blank=True, null=True)

    class Meta:
        unique_together = (("token_id", "smart_contract"),)
        index_together = (("token_id", "smart_contract"),)
