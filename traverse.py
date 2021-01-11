#!/usr/bin/python
from yaml import load
from rstcloth import RstCloth

doc = RstCloth(line_width=180)

def parse_seq(action, index, indent):
    index2 = (1,)

    for subaction in action['seq']:
        parse_action(subaction, index + index2, indent)
        index2 = index2[:-1] + (index2[-1]+1,)

def parse_mix(action, index, indent):
    index2 = (1,)
    for subaction in action['mix']:
        parse_action(subaction, index + index2, indent=indent+1)
        index2 = index2[:-1] + (index2[-1]+1,)

HEADINGS = (doc.h3, doc.h4, doc.h5, doc.h6)

def parse_action(action, index=(0,), indent=0):
    assert type(action) == dict
    index_str = '.'.join(map(str, index[1:])) + '. '

    if 'type' in action and action['type'] == 'section':
        if index_str != '1. ':
            doc._add('\n\n----------\n\n')
        doc.h2(index_str + action['name'])
        doc.newline()
        parse_seq(action, index, indent)
    elif 'seq' in action:
        parse_seq(action, index, indent)
    elif 'mix' in action:
        heading = HEADINGS[indent]
        name = 'name' in action and action['name'] or 'Mix'
        heading(index_str + name + ':')
        doc.newline()
        if 'desc' in action:
            doc.directive('line-block', content=action['desc'])
        parse_mix(action, index, indent)
        doc.newline()
        doc.newline()
    else:
        heading = HEADINGS[indent]
        if 'name' in action:
            heading(index_str + action['name'])
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



if __name__ == '__main__':
    with open('liber-ada.yml', 'r') as liber_ada:
        data = load(liber_ada)
        doc.title('{} - {}'.format(data['name'], data['version']))
        doc.newline()
        parse_action(data['play'])
        doc.print_content()
