import numpy

nacenki = 1.06  # Коэффициент, учитывающий наценки снабженческо-сбытовых организаций
V_sheb = 1.6  # Объемная масса щебня
V_desert = 1.2  # Объемная масса песка
V_grav = 1.4  # Объемная масса гравия


def form_ceh(price_S, S, year_W):  # Расчет удельных капитальных вложений в строительство здания формовочного цеха
    Udel_cap_vloz = price_S * S / year_W  # Стоимость 1 кв.м произ. площ * Произв. площадь цеха / Годовая
    # производительность линии
    return Udel_cap_vloz


def spec_tech(part_cam, system_steam, vent_cam, KIP_n_automatic, V_cam_term, cams,
              price_priyamkov):  # Расчет удельных капитальных вложений в строительство специальных технологических сооружений
    price_yamnih_tunel_cams = (part_cam + system_steam + vent_cam) * V_cam_term \
                              + KIP_n_automatic * cams + price_priyamkov
    return price_yamnih_tunel_cams


def spec_tech_build(year_W, spec_tech):  # Удел. капитальные вложения в строительство спец. техн. сооруж
    return spec_tech / year_W  # Стоимость ямных и туннельных камер тепловой обработки


def payment_tech(p):  # Расчет удельных капитальных вложений на приобретение оборудования
    return sum(list(p))


def sum_form_ceh(form_ceh, spec_tech_build, payment_tech,
                 year_W):  # Общие удел капит. вложения в строительство формовочного цеха
    x = payment_tech / year_W
    return form_ceh + spec_tech_build + x


def price_sheb(opt_price, price_transp, p_clr_vag1, p_clr_vag2, p_razgruz, p_transp_sir_ceh):
    x = opt_price * nacenki + (price_transp + (p_clr_vag1 + p_clr_vag2) + p_razgruz) * V_sheb + p_transp_sir_ceh
    return x


def price_grav(opt_price, price_transp, p_clr_vag1, p_clr_vag2, p_razgruz, p_transp_sir_ceh):
    x = opt_price * nacenki + (price_transp + (p_clr_vag1 + p_clr_vag2) + p_razgruz) * V_grav + p_transp_sir_ceh
    return x


def price_desert(opt_price, price_transp, p_clr_vag1, p_clr_vag2, p_razgruz, p_transp_sir_ceh):
    x = opt_price * nacenki + (price_transp + (p_clr_vag1 + p_clr_vag2) + p_razgruz) * V_desert + p_transp_sir_ceh
    return x


print('Удельные капитальные вложения: ', form_ceh(1, 2, 3),
      '\nСтоимость ямных и туннельных камер тепловой обработки: ',
      spec_tech(1, 2, 3, 4, 5, 6, 7),
      '\nУдел. капитальные вложения в строительство спец. техн. сооруж: ',
      spec_tech_build(3, spec_tech(1, 2, 3, 4, 5, 6, 7)),
      '\nПолная стоимость оборудования: ', payment_tech((1, 2, 3, 4, 5, 6)),
      '\n_____________________________________________________'
      '\nОбщие удел капит. вложения в строительство формовочного цеха: ',
      sum_form_ceh(form_ceh(1, 2, 3), spec_tech_build(3, spec_tech(1, 2, 3, 4, 5, 6, 7)),
                   payment_tech((1, 2, 3, 4, 5, 6)), 3),
      '\n\n\n',
      'Заготовительная цена щебня, гравия, песка',
      '\n',
      '\nЗаготовительная цена на щебень', price_sheb(1, 4, 5, 6, 7, 8),
      '\nЗаготовительная цена на гравий', price_grav(2, 4, 5, 6, 7, 8),
      '\nЗаготовительная цена на песок', price_desert(3, 4, 5, 6, 7, 8)
      )
