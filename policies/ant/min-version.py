from lunar_policy import Check, variable_or_default


def parse_version(v):
    return tuple(int(p) for p in str(v).split("."))


with Check("ant-min-version", "Uses Recent Ant Version in CI/CD") as c:
    cicd = c.get_node(".lang.java.native.ant.cicd")

    if cicd.exists():
        cmds = cicd.get_value_or_default(".cmds", [])
        min_ver = variable_or_default("min_ant_version", "1.10.0")
        for cmd in cmds:
            version = cmd.get("version", "")
            if version:
                meets_min = parse_version(version) >= parse_version(min_ver)
                c.assert_true(meets_min, f"Ant version {version} is below minimum {min_ver}")
    else:
        c.skip("No Ant commands found in CI/CD")
