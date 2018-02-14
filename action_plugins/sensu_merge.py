#!/usr/bin/env python

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        suffix = self._task.args.get('suffix')
        varname = self._task.args.get('var_name')
        mergetype = self._task.args.get('type', 'dict')

        merged = {} if mergetype == 'dict' else []
        mergefunc = merged.update if mergetype == 'dict' else merged.extend
        for var in (v for v in sorted(task_vars.keys()) if v.endswith(suffix)):
            mergefunc(self._templar.template(task_vars[var]))

        return dict(
            ansible_facts={varname: self._templar.template(merged)},
            changed=False
        )
