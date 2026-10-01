<?php
/**
 * Small helpers shared by the templates.
 *
 * @package Studio22
 */

defined( 'ABSPATH' ) || exit;

/**
 * Whether the current page is shown in Arabic (site language, Polylang or WPML).
 *
 * @return bool
 */
function studio22_is_arabic() {
	return 0 === strpos( determine_locale(), 'ar' ) || is_rtl();
}

/**
 * Text from the Customizer in the current language.
 * Each text option is stored twice: "{$key}_en" and "{$key}_ar".
 * Arabic falls back to English when left empty.
 *
 * @param string $key Option key without the language suffix.
 * @return string
 */
function studio22_text( $key ) {
	$defaults = studio22_text_defaults();
	$lang     = studio22_is_arabic() ? 'ar' : 'en';

	$value = get_theme_mod( "studio22_{$key}_{$lang}", $defaults[ $key ][ $lang ] ?? '' );
	if ( '' === trim( (string) $value ) && 'ar' === $lang ) {
		$value = get_theme_mod( "studio22_{$key}_en", $defaults[ $key ]['en'] ?? '' );
	}
	return (string) $value;
}

/**
 * Echo a Customizer text, escaped.
 *
 * @param string $key Option key without the language suffix.
 */
function studio22_e( $key ) {
	echo esc_html( studio22_text( $key ) );
}

/**
 * Plain (non-translated) option with its default.
 *
 * @param string $key Option key without the "studio22_" prefix.
 * @return mixed
 */
function studio22_opt( $key ) {
	$defaults = studio22_option_defaults();
	return get_theme_mod( "studio22_{$key}", $defaults[ $key ] ?? '' );
}

/**
 * WhatsApp number, digits only.
 *
 * @return string
 */
function studio22_whatsapp_number() {
	return preg_replace( '/\D+/', '', (string) studio22_opt( 'whatsapp' ) );
}

/**
 * WhatsApp link with an optional pre-filled message.
 *
 * @param string $message Message text.
 * @return string
 */
function studio22_whatsapp_url( $message = '' ) {
	$number = studio22_whatsapp_number();
	if ( ! $number ) {
		return '';
	}
	$url = 'https://wa.me/' . $number;
	if ( $message ) {
		$url .= '?text=' . rawurlencode( $message );
	}
	return $url;
}

/**
 * Link of the main "book" button: WhatsApp when set, otherwise the contact section.
 *
 * @return string
 */
function studio22_book_url() {
	$wa = studio22_whatsapp_url( studio22_text( 'wa_message' ) );
	return $wa ? $wa : home_url( '/#contact' );
}

/**
 * Social networks supported in the footer.
 *
 * @return array slug => label
 */
function studio22_social_networks() {
	return array(
		'instagram' => 'Instagram',
		'tiktok'    => 'TikTok',
		'youtube'   => 'YouTube',
		'vimeo'     => 'Vimeo',
		'behance'   => 'Behance',
		'linkedin'  => 'LinkedIn',
		'x'         => 'X',
		'snapchat'  => 'Snapchat',
	);
}

/**
 * Inline SVG icon.
 *
 * @param string $name Icon name.
 * @return string
 */
function studio22_icon( $name ) {
	$paths = array(
		'camera'    => '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
		'video'     => '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
		'studio'    => '<path d="M4 20V9l8-5 8 5v11"/><path d="M9 20v-6h6v6"/><circle cx="12" cy="9.5" r="1.2"/>',
		'edit'      => '<path d="M4 7h10M4 12h16M4 17h7"/><circle cx="17" cy="7" r="2"/><circle cx="14" cy="17" r="2"/>',
		'product'   => '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/>',
		'horse'     => '<path d="M7 21v-6l-3-2 2-5 5-4 2 2 4 1 3 4-2 2-3-1-2 3v6"/><circle cx="15.5" cy="7.5" r=".6"/>',
		'drone'     => '<circle cx="5" cy="6" r="2.5"/><circle cx="19" cy="6" r="2.5"/><path d="M7 7.5l3 3.5h4l3-3.5M10 11v3h4v-3M9 17l1.5-3M15 17l-1.5-3"/>',
		'event'     => '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
		'arrow'     => '<path d="M5 12h14M13 6l6 6-6 6"/>',
		'play'      => '<path d="M8 5l11 7-11 7z"/>',
		'whatsapp'  => '<path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-1.8-1.8l.8-1-1-2z"/>',
		'mail'      => '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
		'phone'     => '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
		'pin'       => '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
		'clock'     => '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
		'menu'      => '<path d="M4 8h16M4 16h16"/>',
		'close'     => '<path d="M6 6l12 12M18 6L6 18"/>',
		'instagram' => '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/>',
		'tiktok'    => '<path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 2.8 2.3 4.5 5 5"/>',
		'youtube'   => '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9l5 3-5 3z"/>',
		'vimeo'     => '<path d="M3 8.5l1 1.2s2-1.5 2.6-.7c.6.7 2.7 9 3.4 10.4.6 1.3 2.3 1.2 3.6-.5 1.3-1.6 5.8-6.5 6.4-10 .6-3.4-3.8-3.3-5.8.6 1.8-1 3-.3 2 1.8s-2.6 4-3.1 4c-.6 0-1.5-4.6-2.3-7.6-.8-3.2-4-1.3-7.8.8z"/>',
		'behance'   => '<path d="M3 6h6a3 3 0 0 1 0 6H3zM3 12h6.5a3 3 0 0 1 0 6H3zM14 14h7a3.5 3.5 0 1 0-1 3M15 7h5"/>',
		'linkedin'  => '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
		'x'         => '<path d="M4 4l16 16M20 4L4 20"/>',
		'snapchat'  => '<path d="M12 3c3 0 5 2.2 5 5v2.5l2-.5-1.5 2c.6 2 2.2 3 3.5 3.4-1 .8-2.6.6-3 1.6-.3.8-1.6.3-3 .8-1.1.4-1.8 1.7-3 1.7s-1.9-1.3-3-1.7c-1.4-.5-2.7 0-3-.8-.4-1-2-.8-3-1.6 1.3-.4 2.9-1.4 3.5-3.4L4 10l2 .5V8c0-2.8 2-5 6-5z"/>',
	);
	if ( ! isset( $paths[ $name ] ) ) {
		return '';
	}
	return '<svg class="icon icon-' . esc_attr( $name ) . '" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' . $paths[ $name ] . '</svg>';
}
