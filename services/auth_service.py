from fastapi import HTTPException

def require_role(role: str, allowed_roles: list[str]):
    if not role:
        raise HTTPException(status_code=400, detail="Role is required")

    role = role.lower()

    if role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Access denied")