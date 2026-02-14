def is_eligible_for_loan(age:int,income:float,employment_status:str)->bool:
    return (age>=21) and (income>=5000) and (employment_status=="employed")