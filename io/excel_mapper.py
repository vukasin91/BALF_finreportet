import math
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any

from Models.MatchStatus import MatchStatus

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


def to_decimal(x : Any) -> Decimal:
    if x is None or x == "" or (isinstance(x, float) and math.isnan(x)):
        return Decimal(0)
    s = str(x).strip().replace(",", "")
    try:
        return Decimal(s)
    except (InvalidOperation, ValueError) as e:
        raise ValueError(f"Invalid decimal value: {x!r}") from e

def coerce_match_status(x: Any) -> MatchStatus:
    s = str(x or "").strip().lower()
    if not s :
        raise ValueError(f"Invalid match status: {x!r}")

    return MatchStatus(s)

def to_datetime(x : Any) -> datetime:
    if isinstance(x, datetime):
        return x
    return datetime.fromisoformat(str(x))