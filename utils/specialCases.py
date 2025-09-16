import env

def check_if_module_excluded(lecture: str) -> bool:
    return any(excluded_module.lower() in lecture.lower() for excluded_module in env.EXCLUDE_MODULES)