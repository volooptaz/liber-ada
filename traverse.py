#!/usr/bin/python
from yaml import load
from rstcloth import RstCloth

doc = RstCloth(line_width=180)

def parse_seq(action, indent=0):
    for subaction in action['seq']:
        parse_action(subaction, indent)
    doc.newline()
    doc.newline()

def parse_mix(action, indent=0):
    doc.directive('line-block', content='MIX →')
    doc.newline()
    for subaction in action['mix']:
        parse_action(subaction, indent+1)
    doc.directive('line-block', content='←')
    doc.newline()

def parse_action(action, indent=0):
    assert type(action) == dict

    if 'name' in action:
        if 'type' in action and action['type'] == 'section':
            doc.h2(action['name'])
            doc.newline()
        else:
            doc.directive('line-block', content=action['name'])
            doc.newline()

    if 'url' in action and action['url']:
        assert 'type' in action

        pre = ''
        if action['type'] == 'audio':
            pre += '🔊 '
        elif action['type'] == 'video':
            pre += '🎥 '
        elif action['type'] == 'av':
            pre += '🎥🔊 '
        elif action['type'] == 'screen':
            pre += '🖼️ '

        doc.directive('line-block', content=pre+action['url'])
        doc.newline()
        doc.newline()


    if 'type' in action and action['type'] == 'speech':
        assert 'val' in action
        pre = '💬 '
        doc.directive('epigraph', content=pre+action['val'])
        doc.newline()

    if 'seq' in action:
        parse_seq(action, indent)

    if 'mix' in action:
        parse_mix(action, indent)

if __name__ == '__main__':
    with open('liber-ada.yml', 'r') as liber_ada:
        data = load(liber_ada)
        doc.title('{} - {}'.format(data['name'], data['version']))
        doc.newline()
        parse_action(data['play'])
        doc.print_content()
