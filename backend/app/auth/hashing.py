from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


# ==========================================================
# Hash Password
# ==========================================================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# ==========================================================
# Compatibility Alias
# ==========================================================

def get_password_hash(password: str) -> str:
    return hash_password(password)


# ==========================================================
# Verify Password
# ==========================================================

def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )