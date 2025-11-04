from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
jm1083444 
jm1188022 
jm508262 
jm1188027 
jm1188032 
jm1187593 
jm1015412
jm1134815 
jm1187594 
jm1187643 
jm640291 
jm635851 
jm1186883 
jm1187362 
jm1187368 
jm1118588 
jm1187379 
jm1186482 
jm1186632 
jm1186813 
jm1186364 
jm1186329 
jm1180195 
jm1180203 
jm1186390 
jm651712 
jm565384 
jm1186392 
jm1186405 
jm1186365 
jm1186450
jm1186451 
jm1186455 
jm504446 
jm1186459 
jm1186469 
jm1186477 
jm1186481 
jm1185830 
jm1185358 
jm497371 
jm1185448 
jm1185420 
jm1185425 
jm1185426
jm1185430 
jm1185428 
jm1185419 
jm1184664
jm1185252 
jm368652 
jm296772 
jm1184488 
jm1184491 
jm1184591 
jm1184589 
jm1184446 
jm1183721 
jm1196941 
jm1142760 
jm1183550 
jm1182951 
jm1182955 
jm1079488 
jm583084 
jm1182973 
jm1182971 
jm1182985 
jm1183003 
jm1183397
jm1182576 
jm502016 
jm485676 
jm1182352 
jm1182359 
jm1182387 
jm1181693 
jm1201218
jm1181761
jm1181765 
jm1181715
jm1181729 
jm1175247 
jm1175227 
jm1175281 
jm1181379 
jm1181537 
jm1180773 
jm1026130 
jm416900 
jm1180759 
jm1180616 
jm1180628 
jm1038779 
jm1179802 
jm1179817 
jm1179819 
jm1179609 
jm1179226 
jm1178422 
jm1179134 
jm1179164
jm1173136
jm1173141 
jm360314 
jm1178314 
jm1178420 
jm1092885 
jm1177540 
jm1178306 
jm1177539 
jm1034550 
jm285554 
jm1154263
jm1052231
jm1176761 
jm1176765 
jm1176831 
jm1175453 
jm1169826
jm644781 
jm1175729
jm1175734 
jm1175738 
jm1174343 
jm1174361 
jm1174482 
jm1161644 
jn1173025 
jm1172025
jm1173128 
jm1171968
jm1171973
jm1168498 
jm1168500 
jm1168501 
jm1168908 
jm1168966 
jm1168978 
jm1167619 
jm1167620 
jm1166853 
jm1166862 
jm1166863 
jm1165946 
jm1165930
jm1165892 
jm1164890 
jm1164985 
jm1164871 
jm1164867 
jm1164498 
jm1164499
jm1164826 
jm1164835 
jm1164843
jm641796
jm600484
jm1164468 
jm1162766 
jm1162787
jm1162806 
jm1162620 
jm1161629 
jm1160534 
jm1160559 
jm1160562 
jm1161585 
jm1160529 
jm1158246 
jm563811 
jm1160356 
jm1160395 
jm1158209 
jm1158226 
jm1158343 
jm1145795 
jm1158360 
jm1158120 
jm487520 
jm1155462 
jm1156353 
jm1156356 
jm1156508 
jm1156507 
jm1150922 
jm1147156 
jm1149508 
jm576679 
jm1050140 
jm1150141 
jm1150184 
jm1149102 
jm292976 
jn404275 
jm1071977 
jm1147755 
jn1146464 
jm1150165 
jn1144673 
jm1145389 
jm1147784
jm1134299
jm1030126 
jm172270 
jm475470 
jm1135370 
jm1131688 
jm1067769 
jm1130528 
jm429914 
jm509784 
jm356960
jm1128198
jm1128035 
jm1011742 
jm1101745 
jm1101044 
jm1101047 
jm1101048 
jm1097350 
jm1095846 
jm1098163 
jm487520 
jm1019294
jm1196624
jm1088222
jm1090119 
jm1090135 
jm1091444 
jm1085409 
jm1083964



'''

# 单独下载章节
jm_photos = '''



'''


def env(name, default, trim=('[]', '""', "''")):
    import os
    value = os.getenv(name, None)
    if value is None or value == '':
        return default

    for pair in trim:
        if value.startswith(pair[0]) and value.endswith(pair[1]):
            value = value[1:-1]

    return value


def get_id_set(env_name, given):
    aid_set = set()
    for text in [
        given,
        (env(env_name, '')).replace('-', '\n'),
    ]:
        aid_set.update(str_to_set(text))

    return aid_set


def main():
    album_id_set = get_id_set('JM_ALBUM_IDS', jm_albums)
    photo_id_set = get_id_set('JM_PHOTO_IDS', jm_photos)

    helper = JmcomicUI()
    helper.album_id_list = list(album_id_set)
    helper.photo_id_list = list(photo_id_set)

    option = get_option()
    helper.run(option)
    option.call_all_plugin('after_download')


def get_option():
    # 读取 option 配置文件
    option = create_option(os.path.abspath(os.path.join(__file__, '../../assets/option/option_workflow_download.yml')))

    # 支持工作流覆盖配置文件的配置
    cover_option_config(option)

    # 把请求错误的html下载到文件，方便GitHub Actions下载查看日志
    log_before_raise()

    return option


def cover_option_config(option: JmOption):
    dir_rule = env('DIR_RULE', None)
    if dir_rule is not None:
        the_old = option.dir_rule
        the_new = DirRule(dir_rule, base_dir=the_old.base_dir)
        option.dir_rule = the_new

    impl = env('CLIENT_IMPL', None)
    if impl is not None:
        option.client.impl = impl

    suffix = env('IMAGE_SUFFIX', None)
    if suffix is not None:
        option.download.image.suffix = fix_suffix(suffix)


def log_before_raise():
    jm_download_dir = env('JM_DOWNLOAD_DIR', workspace())
    mkdir_if_not_exists(jm_download_dir)

    def decide_filepath(e):
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)

        if resp is None:
            suffix = str(time_stamp())
        else:
            suffix = resp.url

        name = '-'.join(
            fix_windir_name(it)
            for it in [
                e.description,
                current_thread().name,
                suffix
            ]
        )

        path = f'{jm_download_dir}/【出错了】{name}.log'
        return path

    def exception_listener(e: JmcomicException):
        """
        异常监听器，实现了在 GitHub Actions 下，把请求错误的信息下载到文件，方便调试和通知使用者
        """
        # 决定要写入的文件路径
        path = decide_filepath(e)

        # 准备内容
        content = [
            str(type(e)),
            e.msg,
        ]
        for k, v in e.context.items():
            content.append(f'{k}: {v}')

        # resp.text
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)
        if resp:
            content.append(f'响应文本: {resp.text}')

        # 写文件
        write_text(path, '\n'.join(content))

    JmModuleConfig.register_exception_listener(JmcomicException, exception_listener)


if __name__ == '__main__':
    main()
