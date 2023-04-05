import structlog

log = structlog.get_logger()
log.info("hello, %s!", "world", key="value!", more_than_strings=[1, 2, 3])
#carbon::out 2022-10-07 10:41:29 [info     ] hello, world!   key=value! more_than_strings=[1, 2, 3]