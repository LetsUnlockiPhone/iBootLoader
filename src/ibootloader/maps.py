#
#  iBootLoader | ibootloader
#  maps.py
#
#  Dumps of symbol names for files
#
#  This file is part of iBootLoader. iBootLoader is free software that
#  is made available under the MIT license. Consult the
#  file "LICENSE" that is distributed together with this file
#  for the exact licensing terms.
#
#  Copyright (c) kat 2021.
#

symbols = {
    'srom': {
        't8004si': {
            'credit': 'kat | _kritanta',
            'symbols': {
                0x00000040: 'reset',
                0x0000005C: 'relocate_loop',
                0x00000078: 'relocate_data',
                0x000000A0: 'relocate_data_loop',
                0x000000B0: 'stack_setup',
                0x00000188: 'bss_loop',
                0x00000194: 'bss_done',
                0x000001A0: 'spin',
                0x00000200: 'aSecureromForT8004siCopyright20072014AppleInc',
                0x00000240: 'aRomrelease',
                0x00000280: 'aIboot26510033_0',
                0x00000300: 'Description',
                0x00000304: 'ReleaseCategory',
                0x00000308: 'iBootVersion',
                0x0000030C: 'main',
                0x00000310: 'Start',
                0x0000031C: 'sram_start',
                0x00000328: 'argv',
                0x00000334: 'heap_base',
                0x00000338: '_arm_read_cpsr',
                0x00000350: '_arm_read_ifsr',
                0x00000358: '_arm_read_dfsr',
                0x00000360: '_arm_write_l2_aux_cr',
                0x0000036C: '_arm_read_ifar',
                0x00000374: '_arm_read_extended_feature_regs',
                0x000003CC: '_arm_read_memory_model_feature_regs',
                0x000003E8: '_arm_read_instruction_set_attribute_regs',
                0x00000410: '_arm_read_cr',
                0x00000418: '_arm_write_cr',
                0x00000424: '_arm_read_aux_cr',
                0x0000042C: '_arm_write_aux_cr',
                0x00000438: '_arm_write_dar',
                0x00000444: '_arm_write_ttb',
                0x00000450: '_arm_write_ttbcr',
                0x0000045C: '_arm_read_dfar',
                0x00000464: '_arm_read_main_id',
                0x0000046C: '_arm_read_cache_id',
                0x00000474: '_arm_read_cache_level_id',
                0x00000484: '_arm_write_user_rw_tid',
                0x00000490: '_arm_read_fpexc',
                0x000004A0: '_arm_read_fpscr',
                0x000004F4: '_arm_read_cache_size_selection',
                0x000004FC: '_arm_write_user_ro_tid',
                0x00000508: '_arm_read_pmreg',
                0x000005CC: '_arm_write_pmreg',
                0x00000690: '_arm_read_cache_size_id',
                0x00000698: '_arm_write_sup_tid',
                0x000006A4: '_arm_read_l2_aux_cr',
                0x000006AC: '_arm_write_perip_port_remap',
                0x000006B8: '_arm_read_user_rw_tid',
                0x000006C0: '_arm_write_dprot_region_8',
                0x000006CC: '_arm_read_user_ro_tid',
                0x000006D4: '_arm_write_data_prot_register',
                0x000006E0: '_arm_flush_tlbs',
                0x00000798: '_arm_write_ins_prot_register',
                0x000007A4: '_arm_write_cacheable_registers',
                0x000007B4: '_arm_write_bufferable_register',
                0x000007F0: '_arch_restore_ints',
                0x0000080C: '_arm_enable_fiqs',
                0x0000081C: '_arm_disable_fiqs',
                0x0000082C: '_arm_read_sup_tid',
                0x00000834: '_arm_write_vbar',
                0x0000083C: '_arm_flush_branch_predictor',
                0x0000084C: '_arm_memory_barrier',
                0x00000854: '_arch_halt',
                0x00000860: '_arch_spin',
                0x00000868: '__main',
                0x000014B0: '_timer_get_ticks',
                0x000014B4: '_aic_get_ticks',
                0x000014CC: '_aic_spin',
                0x000014E8: '_timer_ticks_to_usecs',
                0x000014F8: '_timer_usecs_to_ticks',
                0x00001508: '_timer_get_entropy',
                0x00001AD0: '_usbphy_enable_pullup',
                0x00001C88: 'jpt_1C84',
                0x00001ED4: '__src',
                0x00002840: '_synopsys_otg_get_connection_speed',
                0x00002A78: '_synopsys_otg_is_endpoint_stalled',
                0x00003444: '_synopsys_otg_go_on_bus',
                0x000037B0: '_synopsys_otg_start_ep0_out',
                0x00003B34: 'verify_img4_whatever',
                0x00004514: 'aNrpdxekeyekeorpeceseorpdtsgdlodsmodscicedicegcnbbesccescnrpcorpc',
                0x000046B4: 'platform_cache_operation',
                0x0000475C: 'j_j__arm_memory_barrier',
                0x00004784: 'j__chipid_get_minimum_epoch',
                0x000050E4: 'platform_init_setup_clocks',
                0x00005100: 'platform_init_hwpins',
                0x0000527C: 'platform_init_internal_mem',
                0x00005288: 'platform_quiesce_hardware',
                0x000052A0: 'platform_bootprep',
                0x00005308: 'chipid_clear_production_mode',
                0x00005374: '_platform_init_setup_clocks',
                0x00005390: 'platform_get_boot_device',
                0x000053AA: 'jpt_53A6',
                0x000053E4: 'def_53A6',
                0x000053EC: 'platform_enable_boot_interface',
                0x000054CC: 'platform_set_dfu_status',
                0x000054D8: 'platform_get_force_dfu',
                0x000054EC: 'platform_get_request_dfu1',
                0x00005504: 'platform_get_request_dfu2',
                0x00005864: 'platform_get_boot_trampoline',
                0x00005888: '__dst',
                0x00005894: '_chipid_get_production_mode',
                0x000058D4: '_chipid_get_security_domain',
                0x000058E4: '_chipid_get_board_id',
                0x000058F4: '_chipid_get_minimum_epoch',
                0x000059A8: '_charger_has_external',
                0x000059AC: 'chipid_set_fuse_lock',
                0x00005F3C: 'jpt_5F38',
                0x00005F46: 'def_5F38',
                0x00005FD8: 'halt',
                0x00005FE4: 'nullsub_1',
                0x00005FE8: '_platform_power_spin',
                0x00005FEC: 'platform_watchdog_tickle',
                0x0000601C: '_prepare_and_jump',
                0x00006188: '_callout_dequeue',
                0x0000624C: '_debug_init',
                0x00006264: 'nullsub_3',
                0x00006268: '__panic',
                0x00006350: 'doublePanicIn',
                0x00006354: 'panicMacro',
                0x000063FC: 'platform_get_usb_cable_connected',
                0x0000648C: '_enter_critical_section',
                0x000064C8: '_exit_critical_section',
                0x0000681C: '_task_get_current_task',
                0x00006890: 'list_delete',
                0x000068C8: 'task_yield',
                0x0000698C: 'insert_run_q_tail',
                0x000069B0: 'task_start',
                0x000069D4: 'task_exit',
                0x00006A10: 'wait_queue_wake_all',
                0x00006B24: 'wait_queue_wake_one',
                0x00006B54: '_list_remove_head',
                0x00006CE0: '_deep_idle_timeout',
                0x00006CEC: '_system_time',
                0x00006CFC: '_time_has_elapsed',
                0x00006D34: '_spin',
                0x00006D74: 'security_init',
                0x00006EB8: '_security_set_production_override',
                0x0000701C: '_arm_clean_dcache_line',
                0x000070A4: '_arm_clean_invalidate_dcache_line',
                0x000070B0: '_arm_clean_invalidate_dcache',
                0x00007108: '_arm_clean_dcache',
                0x00007160: '_arm_invalidate_dcache',
                0x00007230: '_arm_invalidate_icache',
                0x00007258: '_arm_drain_write_buffer',
                0x000072C8: '_arm_mmu_map_section_range',
                0x00007320: 'jpt_731C',
                0x0000738C: 'def_731C',
                0x000073E0: '_arm_mmu_init',
                0x0000742C: '_arm_fp_init',
                0x0000745C: 'arch_cpu_init',
                0x000074B8: '_arch_cpu_quiesce',
                0x000074E0: '_clocks_init',
                0x00007510: '_arch_get_entropy',
                0x00007540: 'arm_irq',
                0x000075E8: 'arm_fiq',
                0x00007690: 'arm_undefined',
                0x000076C8: 'arm_syscall',
                0x00007700: 'arm_prefetch_abort',
                0x0000773C: 'arm_data_abort',
                0x00007774: '___arm_reserved',
                0x00007AF4: '_usb_init_with_controller',
                0x00007B3C: '_usb_init',
                0x00007B4C: '_usb_quiesce',
                0x00007B74: '_usb_free',
                0x00007B88: '_usb_controller_register',
                0x00007BA8: '__b',
                0x00007BD0: '_usb_controller_stop',
                0x00007BF4: '_usb_controller_deactivate_endpoint',
                0x00007C60: '_stdout_outfunc',
                0x00007E34: 'usb_create_string_descriptor',
                0x000081D6: 'jpt_81D2',
                0x000082D6: 'jpt_82D2',
                0x0000844C: 'def_81D2',
                0x0000863C: '_usb_core_free',
                0x000086B8: '_getDFUImage',
                0x000086E8: '_usb_dfu_init',
                0x00008970: '_usb_dfu_exit',
                0x00008A00: 'image_load',
                0x00009320: '_siphash_aligned',
                0x00009454: 'def_945E',
                0x00009462: 'jpt_945E',
                0x00009690: '_required_size',
                0x000096DC: '_verify_block_checksum',
                0x00009734: '_heap_free',
                0x000098A4: '_calculate_block_checksum',
                0x000098BC: '_heap_memalign',
                0x00009A80: '_alloc_ep0_device_io_request',
                0x00009AB0: '_heap_panic',
                0x00009AC0: '_verify_block_padding',
                0x00009B10: '_free_list_add',
                0x00009C5C: 'heap_verify',
                0x00009E18: 'j__heap_free',
                0x0000A016: 'jpt_A012',
                0x0000A044: 'def_A012',
                0x0000A098: 'jpt_A094',
                0x0000A618: '_vsnprintf',
                0x0000A784: '_longlong_to_hexstring',
                0x0000A7BC: 'kAsciiHexChars',
                0x0000A7C4: '___vsnprintf_chk',
                0x0000A7FC: '_puts',
                0x0000A824: '_putchar',
                0x0000A840: '___strlcat_chk',
                0x0000A85C: '___stack_chk_fail',
                0x0000A884: '_memcpy',
                0x0000ABB0: '_memset',
                0x0000ABC8: '_bzero',
                0x0000ACC0: '_strlen',
                0x0000AD28: '_amc_phy_run_dll_update',
                0x0000AD74: '_strlcat',
                0x0000ADD0: '_strlcpy',
                0x0000B068: '_DERParseBitString',
                0x0000B08C: '_DERParseBoolean',
                0x0000B0B0: '_DERParseInteger',
                0x0000B0F4: '_DERParseInteger64',
                0x0000B160: '_DERDecodeSeqInit',
                0x0000B1B8: '_DERDecodeSeqContentInit',
                0x0000B1C8: '_DERDecodeSeqNext',
                0x0000B210: '_DERParseSequence',
                0x0000B270: '_DERParseSequenceContent',
                0x0000B398: '_Img4DecodeParseLengthFromBuffer',
                0x0000B3C4: '_random_get_bytes',
                0x0000B3E4: '_mib_get_u32',
                0x0000B410: '_random_get_bytes_internal',
                0x0000B500: '_random_get_bytes_noheap',
                0x0000B530: '_chipid_get_current_production_mode',
                0x0000B534: '_platform_get_raw_production_mode',
                0x0000B538: '_platform_get_security_domain',
                0x0000B554: 'j__chipid_get_minimum_epoch_0',
                0x0000B558: '_platform_get_chip_id',
                0x0000B560: '_platform_get_ecid_image_personalization_required',
                0x0000B564: '_platform_get_entropy',
                0x0000B568: '_platform_get_usb_vendor_id',
                0x0000B570: '_power_needs_precharge',
                0x0000B574: '_platform_halt',
                0x0000B578: '_platform_deep_idle',
                0x0000B57C: '_platform_get_usb_manufacturer_string',
                0x0000B584: '_platform_get_usb_device_version',
                0x0000B588: '_platform_get_fuse_modes',
                0x0000B5A4: '_DERImg4DecodeFindInSequence',
                0x0000B5E8: '_DERImg4DecodeContentFindItemWithTag',
                0x0000B614: '_DERImg4DecodeTagCompare',
                0x0000B650: '_DERImg4Decode',
                0x0000B77C: '_DERImg4DecodeUnsignedManifest',
                0x0000B900: '_Img4DecodeInitUnsignedManifest',
                0x0000BB90: '_Img4DecodeGetBooleanFromSection',
                0x0000BBE0: '_Img4DecodeGetPropertyFromSection',
                0x0000BCA0: '_Img4DecodeGetPropertyBoolean',
                0x0000BD20: '_Img4DecodeEvaluateCertificateProperties',
                0x0000BEDC: '_Img4DecodeEvaluateDictionaryProperties',
                0x0001053C: '_arch_get_entropy$shim',
                0x00010548: 'j__arm_clean_invalidate_dcache',
                0x00010554: '_arm_clean_invalidate_dcache_line_2',
                0x00010560: 'j__arm_clean_dcache',
                0x00010578: '_platform_get_chip_revision',
                0x00010584: '_arm_flush_tlbs$shim',
                0x00010590: '_arm_write_cp_access_cr$shim',
                0x000105A8: 'j__arm_enable_fiqs',
                0x000105B4: '_strlen$shim',
                0x000105C0: '_arch_halt$shim',
                0x00010600: 'aNor0',
                0x00010605: 'nil',
                0x00010606: 'aUsb',
                0x0001060A: 'aImg4',
                0x0001060F: 'aIm4p',
                0x00010614: 'aAppleMobileDeviceDfuMode',
                0x00010633: 'aCpid04xCprv02xCpfm02xScep02xBdid02xEcid016llxI',
                0x0001067C: 'aSrtgS',
                0x00010687: 'aNonc',
                0x0001068E: 'a02x',
                0x00010693: 'aSnon',
                0x0001069A: 'aDoublePanicIn',
                0x000106AB: 'doubleNewline',
                0x000106AE: 'newlinePanic',
                0x000106B7: 'colon',
                0x000106BA: 'aIdleTask',
                0x000106C4: 'aNull',
                0x000106CB: 'aPtr',
                0x000106D1: 'a0x',
                0x000106D8: 'aAppleInc',
                0x00012064: 'a0123456789abcdef',
                0x00012074: 'a0123456789abcdef_0',
                0x488001E0: 'current_task',
                0x48800388: 'aBootstrap_0',
                0x4880039C: 'a2kst',
                0x488004A6: 'a0k10',
                0x488004AE: 'aU',
                0x488004B3: 'aAppleSecureBootRootCaG21',
                0x488004DC: 'aAppleInc10',
                0x488004F1: 'aUs0',
                0x488004F7: 'a141219201310z',
                0x48800506: 'a341214201310z0k10',
                0x48800520: 'aAppleSecureBootRootCaG21_0',
                0x48800549: 'aAppleInc10_0',
                0x4880055E: 'aUs0_0',
                0x48800563: 'a0',
                0x4880056A: 'aH',
                0x48802AE8: 'aCpid8004Cprv10Cpfm03Scep01Bdid1eEcid0015243e0e100026',
                0x48802B67: 'aNonc38876290c433a5c8c1f7cf74d0bcef20cec156411cbf654cd5cf957ee6',
                0x48802F30: 'aKatskatskatskatskatskatskatskatskatskatskatskatskatskatskatskats_0',
                0x48805F1F: 'aHex',
                0x48805F28: 'aQx',
                0x48805F2C: 'aKats',
                0x488060F0: 'aIdleTask_1',
                0x48806104: 'a2kst_1',
                0x48807BA1: 'ebolink',
                0x48810240: 'aApppplleeMmoobbiilleeDdeevviicceeDdffuuMmooddee',
                0x48810448: 'aUsb_0',
                0x488104C0: 'aKatskatskatskatskatskatskatskatskatskatskatskatskatskatskatskats',
                0x48811500: 'aCmemcmem'
            }
        }
    }
}