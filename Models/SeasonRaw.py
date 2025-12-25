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



