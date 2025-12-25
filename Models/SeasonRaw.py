from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from MatchStatus import MatchStatus


@dataclass(slots=True, kw_only=True)
class SeasonRaw:
    id : int
    round_no : int
    home_team : str
    away_team : str
    match_start : datetime
    match_date : datetime
    venue : str
    league : str
    manager : str
    match_type : str
    leftover : bool
    status : MatchStatus
    main_referee_name : str
    secondary_referee_name : str
    referee_score : int
    delegate_name : str
    date_of_handover : datetime
    delegate_handover : bool
    handover_to_who : str

    #money type with safe defaults
    total_match_paid: Decimal("0")
    cash_payment: Decimal("0")
    bank_payment: Decimal("0")
    deposit_payment: Decimal("0")
    voucher_payment: Decimal("0")
    venue_payment_cash: Decimal("0")
    venue_payment_bank_account: Decimal("0")
    referee_payment: Decimal("0")
    secondary_referee_payment: Decimal("0")
    delegate_payment: Decimal("0")
    manager_payment : Decimal("0")
    deposit_top_of_bank_account : Decimal("0")
    deposit_top_of_cash : Decimal("0")
    player_registration_fee_bank_account : Decimal("0")
    player_registration_fee_Cash : Decimal("0")
    misc_income : Decimal("0")
    additional_costs : Decimal("0")

COLMAP = {
    "ID": "id",
    "Kolo" : "round_no",
    "Domacin" : "home_team",
    "Gost" : "away_team",
    "Vreme igranja" : "match_date",
    "Balon igranja" : "venue",
    "Liga" : "league",
    "Menadzer" : "manager",
    "Tip meča (liga, kup, p/off)" : "match_type",
    "Zaostala utakmica" : "leftover",
    "Status" : "status",
    "Termin plaćen" : "total_match_paid",
    "Način placanja - keš" : "cash_payment",
    "Način placanja - racun" : "bank_payment",
    "Način placanja - vaucer" : "voucher_payment",
    "Način placanja - depozit" : "deposit_payment",
    "Balon plaćen - kes" : "venue_payment_cash",
    "Balon plaćen - racun" : "venue_payment_bank_account",
    "Cena gl sudije" : "referee_payment",
    "Glavni sudija" : "main_referee_name",
    "Cena pom sudije" : "secondary_referee_payment",
    "Pomoćni sudija" : "secondary_referee_name",
    "Ocena" : "score",
    "Cena delegata" : "delegate_payment",
    "Delegat (ime i prezime)" : "delegate_name",
    "Naknada za utakmicu" : "manager_payment",
    "Dopuna depozita - racun" : "deposit_top_of_bank_account",
    "Dopuna depozita - kes" : "deposit_top_of_cash",
    "Prijava igrača - racun" : "player_registration_fee_bank_account",
    "Prijava igrača - kes" : "player_registration_fee_Cash",
    "Ostale uplate - donacije" : "misc_income",
    "Minusi" : "additional_costs",
    "Datum predaje" : "date_of_handover",
    "Delegat predao" : "delegate_handover",
    "Predao kome" : "handover_to_who"
}


