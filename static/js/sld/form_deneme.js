$(document).ready(function () {
    const kapi_tipi_div = $('#div_id_kapi_tipi');
    const gecis_genisligi_div = $('#div_id_gecis_genisligi');
    const gecis_yuksekligi_div = $('#div_id_gecis_yuksekligi');
    const toplam_genislik_div = $('#div_id_toplam_genislik');
    const toplam_yukseklik_div = $('#div_id_toplam_yukseklik');
    const mekanizma_genisligi_div = $('#div_id_mekanizma_genisligi');
    const ustluk_div = $('#div_id_ustluk');
    const cam_div = $('#div_id_cam');
    const acilis_yonu_div = $('#div_id_acilis_yonu');
    const bitis_div = $('#div_id_bitis');
    const opsiyonlar_div = $('#div_id_opsiyonlar');
    const radar_aktivasyonlar_div = $('#div_id_radar_aktivasyonlar');

    let selected_door = '';

    const doors = [
        {
            name: "Düz",
            types: [
                {
                    name:  "TEK HAREKETLİ",
                    short: "th_standart",
                    image: "/static/img/sld/th_standart.png",
                },
                {
                    name:  "TEK SBT. + TEK HRK.",
                    short: "ts_th_standart",
                    image: "/static/img/sld/ts_th_standart.png",
                },
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_standart",
                    image: "/static/img/sld/ih_standart.png",
                },
                {
                    name:  "İKİ SBT. + İKİ HRK.",
                    short: "is_ih_standart",
                    image: "/static/img/sld/is_ih_standart.png",
                },
            ]
        },
        {
            name: "Cam",
            types: [
                {
                    name:  "TEK HAREKETLİ",
                    short: "th_cam",
                    image: "/static/img/sld/th_cam.png",
                },
                {
                    name:  "TEK SBT. + TEK HRK.",
                    short: "ts_th_cam",
                    image: "/static/img/sld/ts_th_cam.png",
                },
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_cam",
                    image: "/static/img/sld/ih_cam.png",
                },
                {
                    name:  "İKİ SBT. + İKİ HRK.",
                    short: "is_ih_cam",
                    image: "/static/img/sld/is_ih_cam.png",
                },
            ]
        },
        {
            name: "Teleskopik",
            types: [
                {
                    name:  "İKİ HAREKETLİ",
                    short: "ih_teleskop",
                    image: "/static/img/sld/ih_teleskop.png",
                },
                {
                    name:  "İKİ HRK. + TEK SBT.",
                    short: "ih_ts_teleskop",
                    image: "/static/img/sld/ts_ih_ts_teleskop.png",
                },
                {
                    name:  "DÖRT HAREKETLİ",
                    short: "dh_teleskop",
                    image: "/static/img/sld/dh_teleskop.png",
                },
                {
                    name:  "DÖRT HRK. + İKİ SBT.",
                    short: "dh_is_teleskop",
                    image: "/static/img/sld/is_dh_is_teleskop.png",
                },
            ]
        },
    ];


    acilis_yonu_div.hide();
    gecis_genisligi_div.hide();
    gecis_yuksekligi_div.hide();
    toplam_genislik_div.hide();
    toplam_yukseklik_div.hide();
    mekanizma_genisligi_div.hide();
    ustluk_div.hide();
    cam_div.hide();
    bitis_div.hide();
    opsiyonlar_div.hide();
    radar_aktivasyonlar_div.hide();

    cam_div.find('input').removeAttr('required');
    bitis_div.find('input').removeAttr('required');


    // Kapı tiplerini alma
    let door_name_list = [];

    $.each(doors, function (i, door) {
        door_name_list.push(door['name'])
    });
    // Yeni bi select box oluşturma
    let door_name = kapi_tipi_div.clone().attr('id', 'door_name');
    door_name.find('select').removeAttr('id');
    door_name.find('select').attr('name', 'door_name');
    kapi_tipi_div.after(door_name);
    kapi_tipi_div.hide();


    // select box doldurma işlemleri.
    door_name.find('option').not(':first').remove();

    $(door_name_list).each(function (i, door) {
        door_name.find('option').last().after(`<option value="${door}">${door}</option>`)
    });

    door_name.find('select').change(function () {
        $('.types').remove();

        let name = $(this).val();
        let door = doors.find(door => door.name === name);
        let types_div = $('<div/>',{
            'class': 'types form-group'
        }).insertAfter(door_name);

        $(door.types).each(function (i, typ) {
            // TODO edit image url with varibale
            let bg = $('<div/>', {
                'class': 'background',
                'style': 'background-image: url(' + typ.image + ')'
            }).appendTo(types_div);

            bg.append(`<p>${typ.name}</p>`);

            $('<input/>', {
                'name': 'type-of-door',
                'value': typ.short,
                'type': 'radio',
            }).appendTo(bg);
        });

        $('input[name=type-of-door]').click(function(){
            selected_door = $(this).val();
            $('select[name=door_type] option').removeAttr('selected');
            $('select[name=door_type] option[value='+ selected_door +']').prop('selected', 'selected');

            if(selected_door === 'th_standart' || selected_door === 'ih_standart'){

                toplam_genislik_div.hide();
                toplam_yukseklik_div.show();
                mekanizma_genisligi_div.show();
                ustluk_div.hide();
                gecis_genisligi_div.show();
                gecis_yuksekligi_div.show();

                toplam_genislik_div.find('input').val('');
                toplam_yukseklik_div.find('input').val('');

                gecis_yuksekligi_div.find('input').change(function () {
                    toplam_yukseklik_div.find('input').val(parseInt($(this).val()) + 110);
                });
                gecis_genisligi_div.find('input').change(function () {
                    mekanizma_genisligi_div.find('input').val(parseInt($(this).val()));
                });

            }
            else if (selected_door === 'ts_th_standart' || selected_door === 'is_ih_standart'){

                gecis_genisligi_div.show();
                gecis_yuksekligi_div.show();
                mekanizma_genisligi_div.hide();
                toplam_yukseklik_div.show();
                toplam_genislik_div.show();
                ustluk_div.show();

                ustluk_div.find('input').checked = false;
                mekanizma_genisligi_div.find('input').val('');

                // toplam yükseklik ve genişliği hesaplama
                gecis_yuksekligi_div.find('input').change(function () {
                    toplam_yukseklik_div.find('input').val(parseInt($(this).val()) + 120);
                });
                gecis_genisligi_div.find('input').change(function () {
                    toplam_genislik_div.find('input').val($(this).val() * 2);
                });

            } // else if

            if(selected_door === 'ts_th_standart'  || selected_door === 'th_standart'){
                acilis_yonu_div.show();
            }
            else{
                acilis_yonu_div.hide();
                acilis_yonu_div.find('option:selected').prop('selected', false).removeAttr('selected');
                acilis_yonu_div.find('option:first').prop('selected', 'selected');

            }
        });

        $('input[name=pass_height]').change(function () {
            if ((selected_door === 'ts_th_standart' ||
                selected_door === 'is_ih_standart') &&
                !ustluk_div.find('input').first().checked){
                // calculation of pass_heigth
                ustluk_div.find('input').change(function () {
                });
            }
        });
    });
});