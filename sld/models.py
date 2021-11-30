from django.db import models


class SldModel(models.Model):
    # Burdaki isimlendirmeler js tarafında da aynı şekilde olmalıdır!
    # Herhanbi bi değişiklikte dikkatli olunmalı
    KAPI_TIPLERI = (
        ('ts_th_standart', 'STANDART TEK SBT. + TEK HRK.'),
        ('ih_standart', 'STANDART IKI HAREKETLI'),
        ('ts_th_cam', 'CAM - TEK SBT. + TEK HRK.'),
        ('ih_cam', 'CAM - IKI HAREKETLI'),
        ('ih_ts_teleskop', 'TELESKOPIK - IKI HRK. + TEK SBT.'),
        ('dh_teleskop', 'TELESKOPIK - DORT HAREKETLI'),
    )

    OPSIYON_LISTESI = (
        ('konum_anahtari_standart', 'Konum Anahtarı Standart'),
        ('konum_anahtarı_sivaustu', 'Konum Anahtarı Siva UstU'),
        ('el_terminali', 'El Terminali'),
        ('acil_stop', 'Acil Stop'),
        ('elektronik_kilit', 'Elektronik Kilit'),
        ('batarya', 'Batarya'),
    )

    RADAR_AKTIVASYON_SECENEKLERI = (
        ('mikrodalga_radar', 'Mikrodalga Radar'),
        ('combineRadar_safety_activation', 'CombineRadar Safety - Activation'),
        ('yaklasim_sensoru', 'Yaklaşım Sensoru'),
        ('emniyet_fotoseli', 'Emniyet Fotoseli'),
    )
    TESLIM_SEKLI = (
        ('Kapida Teslim', 'Kapida Teslim'),
        ('Nakliye Ambarina Sevkiyat', 'Nakliye Ambarina Sevkiyat'),
        ('Montaj Dahil', 'Montaj Dahil'),
    )
    PAKETLEME_SEKLI = (
        ('Sandikli Paketleme', 'Sandikli Paketleme'),
        ('Standart Paketleme', 'Standart Paketleme'),
    )
    SON_BITISLER = (
        ('Ral Boya', 'Ral Boya'),
        ('Mat Eloksal', 'Mat Eloksal'),
        ('Renkli Mat Eloksal', 'Renkli Mat Eloksal'),
        ('304 Kalite Mat Paslanmaz', '304 Kalite Mat Paslanmaz'),
        ('304 Kalite Ayna Paslanmaz', '304 Kalite Ayna Paslanmaz'),
        ('304 Kalite Satine Paslanmaz', '304 Kalite Satine Paslanmaz'),
        ('316 Kalite Mat Paslanmaz', '316 Kalite Mat Paslanmaz'),
        ('316 Kalite Ayna Paslanmaz', '316 Kalite Ayna Paslanmaz'),
        ('316 Kalite Satine Paslanmaz', '316 Kalite Satine Paslanmaz'),
    )
    CAM_TIPLERI_STANDART = (
        ('4+4 Seffaf Lamine', '4+4 Seffaf Lamine'),
        ('5+5 Seffaf Lamine', '5+5 Seffaf Lamine'),
        ('6+6 Seffaf Lamine', '6+6 Seffaf Lamine'),
        ('4+4 Opak Lamine', '4+4 Opak Lamine'),
        ('5+5 Opak Lamine', '5+5 Opak Lamine'),
        ('6+6 Opak Lamine', '6+6 Opak Lamine'),
        ('8 mm Temperli', '8 mm Temperli'),
        ('10 mm Temperli', '10 mm Temperli'),
        ('12 mm Temperli', '12 mm Temperli'),
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    crm = models.CharField('CRM No', max_length=10, blank=False, null=False)
    firma_bilgileri = models.CharField(verbose_name='Firma', max_length=150)
    sevk_adresi = models.CharField('Sevk Adresi', max_length=80)
    olusturma_tarihi = models.DateTimeField('Olusturma Tarihi', blank=True, null=True, auto_now_add=True)
    teslim_tarihi = models.DateField('Teslim Tarihi')
    teslim_sekli = models.CharField('Teslim Sekli', choices=TESLIM_SEKLI, max_length=35)
    paketleme_sekli = models.CharField('Paketleme Sekilleri', choices=PAKETLEME_SEKLI, max_length=50)
    cam = models.CharField('Cam', choices=CAM_TIPLERI_STANDART, max_length=25, blank=True)
    bitis = models.CharField('Renk', choices=SON_BITISLER, max_length=27, blank=True)
    notlar = models.TextField('Notlar', blank=True, null=True)
    hazirlayan = models.CharField('Hazırlayan', max_length=200)
    imalat_sorumlusu = models.CharField('Imalat Sorumlusu', blank=True, null=True, max_length=40)
    acilis_yonu = models.CharField('Acilis Yonu', max_length=3,
                                   choices=(('sag', 'SAG'), ('sol', 'SOL')), null=True, blank=True)
    ustluk = models.BooleanField('UstlUk Var Mi?', default=False)
    kapi_tipi = models.CharField('Kapi Tipi', choices=KAPI_TIPLERI, max_length=30)
    gecis_genisligi = models.PositiveSmallIntegerField('Gecis Genisligi')
    gecis_yuksekligi = models.PositiveSmallIntegerField('Gecis Yüksekligi')
    toplam_genislik = models.PositiveSmallIntegerField('Toplam Genislik', null=True, blank=True)
    toplam_yukseklik = models.PositiveSmallIntegerField('Toplam Yükseklik', null=True, blank=True)
    mekanizma_genisligi = models.PositiveSmallIntegerField('Mekanizma Genisligi', null=True, blank=True)
    opsiyonlar = models.CharField('Opsiyon Listesi', blank=True, null=True, max_length=250)
    radar_aktivasyonlar = models.CharField('Radar ve Aktivasyon Secenekleri', blank=True, null=True, max_length=250)

    # opsiyonlar ve radar aktivasyonları aralarında boş bırakılarak "*_LIST" içerisindeki ilk verilerden olusturulmalı
    # ornek: "acil_stop batarya"

    class Meta:
        db_table = 'Sld'
        verbose_name = 'SLD Kayar Kapi'
        verbose_name_plural = 'SLD Kayar Kapilar'

    def __str__(self):
        return f'{self.crm} - {self.firma_bilgileri} - {self.kapi_tipi}'
    # crm no ve firma isimleri database ve admin panelinde gozukur.
