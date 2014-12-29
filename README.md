YAML to TOML converter
======================

This is a tool which helps to convert YAML data to TOML format using Jinja2
template.


Motivation
----------

[YAML](http://www.yaml.org/) and [TOML](https://github.com/toml-lang/toml) are
languages used to describe a data structures often used in configuration files.
TOML is relatively young language which is trying minimalize the configuration
file format.

Sometimes it's necessary to use YAML as the description of the configuration file
and then it's necessary to do the conversion. For example in
[Ansible](http://ansible.com), everything is defied as YAML and if a program
managed by Ansible (e.g. [InfluxDB](http://influxdb.com)) needs to have config
file in TOML format, it's necessay to convert the YAML data to TOML format via
template.


Coversion
---------

A YAML file can be converted as follows:

```
$ ./yaml2toml.py -y ./tests/example.yaml
```

or

```
$ cat ./tests/example.yaml | ./yaml2toml.py
```

It is also possible to use Ansible playbook to do the conversion:

```
$ ansible-playbook --diff -i hosts ./yaml2toml_playbook.yaml
```

The output of the Ansible playbook conversion is then in the file `output.toml`.


Limitation
----------

Jinja2 doesn't provide any filters for `datetime` so this converter fails if you
use `datetime` types in the YAML data. The workaround is to quote the `datetime`
values.


Files
-----

- `yaml2toml.py` - conversion script written in Python
- `yaml2toml_macro.j2` - Jinja2 template with the macro which does the conversion
   from YAML to TOML
- `yaml2toml_example.j2` - Jinja2 template calling the yaml2toml macro
- `yaml2toml.yaml` - Ansible playbook doing the conversion
- `hosts` - inventory file used by Ansible
- `tests/*` - testing files


Requirements
------------

- Python v2
- `jinja` Python module
- `yaml` Python module
- Ansible (optional)


License
-------

MIT


Author
------

Jiri Tyr
