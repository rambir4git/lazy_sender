# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 02:35:59 2020

@author: Happy
"""

import sys
import time
import boto3
from botocore.exceptions import ClientError

SENDER = "GetMyMettle <cs@getmymettle.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
#RECIPIENT = "rambir.git@gmail.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
CONFIGURATION_SET = "Emailer"

# AWS Region you're using for Amazon SES.
AWS_REGION = "ap-south-1"

# The subject line for the email.
SUBJECT = "Mettle give you that extra power for your gym rountine."

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Offering up to 45% off on out entire range of Protein Supplements.\r\n"
             "USE CODE: SPECIAL40\r\n"
             "Get Extra 5% off on with choosing prepaid payment method.\r\n"
             "Download our GetMyMettle android app form Google's Playstore."
            )
            
# The HTML body of the email.
BODY_HTML = """

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
	<!--[if gte mso 9]>
	<xml>
		<o:OfficeDocumentSettings>
		<o:AllowPNG/>
		<o:PixelsPerInch>96</o:PixelsPerInch>
		</o:OfficeDocumentSettings>
	</xml>
	<![endif]-->
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="format-detection" content="date=no" />
	<meta name="format-detection" content="address=no" />
	<meta name="format-detection" content="telephone=no" />
	<meta name="x-apple-disable-message-reformatting" />
    <!--[if !mso]><!-->
   	<link href="https://fonts.googleapis.com/css?family=Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet"/>
    <!--<![endif]-->
	<title>Email Template</title>
	<!--[if gte mso 9]>
	<style type="text/css" media="all">
		sup { font-size: 100% !important; }
	</style>
	<![endif]-->
	

	<style type="text/css" media="screen">
		/* Linked Styles */
		body { padding:0 !important; margin:0 !important; display:block !important; min-width:100% !important; width:100% !important; background:#ffffff; -webkit-text-size-adjust:none }
		a { color:#66b7f0; text-decoration:none }
		p { padding:0 !important; margin:0 !important } 
		img { -ms-interpolation-mode: bicubic; /* Allow smoother rendering of resized image in Internet Explorer */ }
		.mcnPreviewText { display: none !important; }
		
		/* Mobile styles */
		@media only screen and (max-device-width: 480px), only screen and (max-width: 480px) {
			.mobile-shell { width: 100% !important; min-width: 100% !important; }
			
			.m-center { text-align: center !important; }
			
			.center { margin: 0 auto !important; }
			
			.td { width: 100% !important; min-width: 100% !important; }

			.m-br-3 { height: 3px !important; }
			.m-br-4 { height: 4px !important; background: #f4f4f4 !important; }
			.m-br-15 { height: 15px !important; }
			.m-br-25 { height: 25px !important; }

			.m-td,
			.m-hide { display: none !important; width: 0 !important; height: 0 !important; font-size: 0 !important; line-height: 0 !important; min-height: 0 !important; }

			.m-block { display: block !important; }

			.fluid-img img { width: 100% !important; max-width: 100% !important; height: auto !important; }

			.column-top,
			.column { float: left !important; width: 100% !important; display: block !important; }

			.content-spacing { width: 15px !important; }

			.m-bg { display: block !important; width: 100% !important; height: auto !important; background-position: center center !important; }

			.h-auto { height: auto !important; }

			.plr-15 { padding-left: 15px !important; padding-right: 15px !important; }

			.w-2 { width: 2% !important; }
			.w-49 { width: 49% !important; }

			.pb-4 { padding-bottom: 4px !important; }
			.pb-15 { padding-bottom: 15px !important; }

			.pt-0 { padding-top: 0 !important; }

			.h1,
			.h1-white { font-size: 36px !important; line-height: 46px !important; }
			.h2 { font-size: 26px !important; line-height: 36px !important; }

			.text-btn-large,
			.text-btn-large-white { padding: 15px 25px !important; }
			.text-btn,
			.text-btn-1,
			.text-btn-1-white { padding: 12px 15px !important; }
		}
	</style>
</head>
<body class="body" style="padding:0 !important; margin:0 !important; display:block !important; min-width:100% !important; width:50% !important; background:#ffffff; -webkit-text-size-adjust:none;">
<body class="body" style="padding:0 !important; margin:0 !important; display:block !important; min-width:100% !important; width:50% !important; background:#ffffff; -webkit-text-size-adjust:none;">
	<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
		<tr>
			<td align="center" valign="top">

				<!-- Header -->
				<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
					<tr>
						<td align="center" valign="top">
							<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
								<tr>
									<td class="img-center" style="padding: 45px 15px; font-size:0pt; line-height:0pt; text-align:center;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/06/logomettle.png" width="225" height="50" border="0" alt="" /></a></td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
				<!-- END Header -->

				<!-- Nav -->
				
				<!-- END Nav -->

				<!-- Main -->
				<table width="100%" border="0" cellspacing="0" cellpadding="0">
					<tr>
						<td>
							<!-- Section - Intro -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td valign="top">
										<table width="100%" border="0" cellspacing="0" cellpadding="0">
											<tr>
												<td class="img" height="245" bgcolor="#f4f4f4" style="font-size:0pt; line-height:0pt; text-align:left;">&nbsp;</td>
											</tr>
										</table>
									</td>
									<td align="center" valign="top" width="650" class="mobile-shell">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td>
													<table width="100%" border="0" cellspacing="0" cellpadding="0">
														<tr>
															<td class="fluid-img" style="padding-bottom: 40px; font-size:0pt; line-height:0pt; text-align:left;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/10/WhatsApp-Image-2020-10-28-at-11.03.54-AM.jpeg" width="750" height="450" border="0" alt="" /></a></td>
														</tr>
														<tr>
															<td class="plr-15" style="padding: 0 60px 50px 60px;">
																<table width="100%" border="0" cellspacing="0" cellpadding="0">
																	<tr>
																		<td class="h1 fw-medium" style="padding-bottom: 20px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:40px; line-height:50px; text-align:center; font-weight:500;">
																			Offering up to 45% off on our entire range of Protein Supplements.
																		</td>
																	</tr>
																	<tr>
																		<td class="text-1" style="padding-bottom: 30px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:16px; line-height:30px; text-align:center;">
																			Offering a wide range of Nutritious & Delicious snacks along with goodness to meet your day to day Power needs.
																		</td>
																	</tr>
																	<tr>
																		<td align="center" style="padding-bottom: 30px;">
																			<!-- Button -->
																			<table border="0" cellspacing="0" cellpadding="0">
																				<tr>
																					<td class="text-btn-large" bgcolor="#ffffff" style="color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:14px; line-height:18px; text-align:center; border:1px solid #e5e5e5; padding:15px 35px;">
																						<a href="https://getmymettle.com/shop/" target="_blank" class="link-2" style="color:#4a4a4a; text-decoration:none;"><span class="link-2" style="color:#4a4a4a; text-decoration:none;">BUY NOW</span></a>
																					</td>
																				</tr>
																			</table>
																			<!-- END Button -->
																		</td>
																	</tr>
																	<tr>
																		<td class="text-2" style="color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:11px; line-height:15px; text-align:center;">
																			<a href="https://getmymettle.com" target="_blank" class="link-2-u" style="color:#4a4a4a; text-decoration:underline;"><span class="link-2-u" style="color:#4a4a4a; text-decoration:underline;">VISIT OUR STORE</span></a>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</table>
									</td>
									<td valign="top">
										<table width="100%" border="0" cellspacing="0" cellpadding="0">
											<tr>
												<td class="img" height="245" bgcolor="#f4f4f4" style="font-size:0pt; line-height:0pt; text-align:left;">&nbsp;</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Intro -->
						</td>
					</tr>
					
					<tr>
						<td>
							<!-- Section - Separator Grey 50px - 1 -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
								<tr>
									<td align="center" valign="top">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td class="img" height="50" style="font-size:0pt; line-height:0pt; text-align:left;">&nbsp;</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Separator Grey 50px - 1 -->
						</td>
					</tr>
					
					<tr>
						<td>
							<!-- Section - Discount -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
								<tr>
									<td align="center" valign="top">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td style="padding-bottom: 50px;">
													<table width="100%" border="0" cellspacing="0" cellpadding="0">
														<tr>
															<td align="center" style="padding-bottom: 25px;">
																<!-- Label -->
																<table border="0" cellspacing="0" cellpadding="0">
																	<tr>
																		<td class="text-2-white fw-medium" bgcolor="#ee6e67" style="padding: 5px 10px; color:#ffffff; font-family:'Poppins', Arial,sans-serif; font-size:11px; line-height:15px; text-align:center; font-weight:500;">
																			SPECIAL OFFER
																		</td>
																	</tr>
																</table>
																<!-- END Label -->
															</td>
														</tr>
														<tr>
															<td class="h2 to-left fw-semibold m-center plr-15" style="padding: 0 30px 30px 30px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:30px; line-height:40px; text-align:left; font-weight:600;">
																Get flat 40% off on sports supplements on your every order.
															</td>
														</tr>
														<tr>
															<td class="plr-15" style="padding: 0 30px;">
																<table width="100%" border="0" cellspacing="0" cellpadding="0">
																	<tr>
																		<th class="column" width="320" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
																			<div class="fluid-img" style="font-size:0pt; line-height:0pt; text-align:left;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/08/Creatine-Monohydrate-Front-M-1.jpg" border="0" width="320" height="350" alt="" /></a></div>
																		</th>
																		<th class="column" width="30" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;"><div style="font-size:0pt; line-height:0pt;" class="m-br-15"></div>
</th>
																		<th class="column" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
																			<table width="100%" border="0" cellspacing="0" cellpadding="0">
																				<tr>
																					<td class="text-1 to-left m-center" style="padding-bottom: 30px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:16px; line-height:30px; text-align:left;">
																						After heavy exercises and workouts, they provide complete nutrition to our body which then helps in muscle recovery and leading to Muscle Growth.
																					</td>
																				</tr>
																				<tr>
																					<td class="text to-left m-center" style="padding-bottom: 15px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:14px; line-height:18px; text-align:left;">
																						USE THIS COUPON AT CHECKOUT:
																					</td>
																				</tr>
																				<tr>
																					<td align="left">
																						<table border="0" cellspacing="0" cellpadding="0" class="center">
																							<tr>
																								<td class="h4 fw-semibold" style="padding: 10px 15px; border: 2px dashed #d5d5d5; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:20px; line-height:24px; text-align:center; font-weight:600;">
																									SPECIAL40
																								</td>
																							</tr>
																						</table>
																					</td>
																				</tr>
																			</table>
																		</th>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Discount -->
						</td>
					</tr>

					<tr>
						<td>
							<!-- Section - Separator White 50px - 1 -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
								<tr>
									<td align="center" valign="top">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td class="img" height="50" style="font-size:0pt; line-height:0pt; text-align:left;">&nbsp;</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Separator White 50px - 1 -->
						</td>
					</tr>

					<tr>
						<td>
							<!-- Section - 2 Cols -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
								<tr>
									<td align="center" valign="top">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td class="plr-15" style="padding-bottom: 50px;">
													<!-- Section Title -->
													<table width="100%" border="0" cellspacing="0" cellpadding="0">
														<tr>
															<td class="h3 fw-medium" style="padding-bottom: 20px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:22px; line-height:26px; text-align:center; font-weight:500;">
																Your Gym Partner
															</td>
														</tr>
													</table>
													<!-- END Section Title -->
												
													<!-- 2 Cols -->
													<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
														<tr>
															<td style="padding: 10px 10px 0 10px;">
																<table width="100%" border="0" cellspacing="0" cellpadding="0">
																	<tr mc:repeatable>
																		<td style="padding-bottom: 10px;">
																			<table width="100%" border="0" cellspacing="0" cellpadding="0">
																				<tr>
																					<th class="column-top" valign="top" width="310" bgcolor="#ffffff" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
																						<table width="100%" border="0" cellspacing="0" cellpadding="0">
																							<tr>
																								<td class="plr-15" style="padding: 50px 15px;">
																									<table width="100%" border="0" cellspacing="0" cellpadding="0">
																										<tr>
																											<td class="fluid-img centered" style="padding-bottom: 25px; font-size:0pt; line-height:0pt; text-align:center;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/10/Super-Whey-Gold-Strawberry-Front-2.jpg" width="250" height="250" border="0" alt="" /></a></td>
																										</tr>
																										<tr>
																											<td class="h3 fw-light" style="padding-bottom: 15px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:22px; line-height:26px; text-align:center; font-weight:300;">
																												Mettle Super Whey Gold (Strawberry, 1kg)
																											</td>
																										</tr>
																										<tr>
																											<td class="h4-2 fw-semibold" style="padding-bottom: 20px; color:#979797; font-family:'Poppins', Arial,sans-serif; font-size:20px; line-height:24px; text-align:center; font-weight:600;">
																												<span class="link" style="color:#66b7f0; text-decoration:none;">MRP 1999</span>
																											</td>
																										</tr>
																										<tr>
																											<td align="center">
																												<!-- Button -->
																												<table border="0" cellspacing="0" cellpadding="0">
																													<tr>
																														<td class="text-btn" bgcolor="#ffffff" style="color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:14px; line-height:18px; text-align:center; border:1px solid #e5e5e5; padding:12px 20px;">
																															<a href="https://getmymettle.com/product/mettle-super-whey-gold-strawberry-1-kg/" target="_blank" class="link-2" style="color:#4a4a4a; text-decoration:none;"><span class="link-2" style="color:#4a4a4a; text-decoration:none;">SHOP NOW</span></a>
																														</td>
																													</tr>
																												</table>
																												<!-- END Button -->
																											</td>
																										</tr>
																									</table>
																								</td>
																							</tr>
																						</table>
																					</th>
																					<th class="column-top" valign="top" width="10" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"><div style="font-size:0pt; line-height:0pt;" class="m-br-10"></div>
</th>
																					<th class="column-top" valign="top" width="310" bgcolor="#ffffff" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
																						<table width="100%" border="0" cellspacing="0" cellpadding="0">
																							<tr>
																								<td class="plr-15" style="padding: 50px 15px;">
																									<table width="100%" border="0" cellspacing="0" cellpadding="0">
																										<tr>
																											<td class="fluid-img centered" style="padding-bottom: 25px; font-size:0pt; line-height:0pt; text-align:center;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/10/Super-Elite-Gainer-Cookie-Front-1.jpg" width="250" height="250" border="0" alt="" /></a></td>
																										</tr>
																										<tr>
																											<td class="h3 fw-light" style="padding-bottom: 15px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:22px; line-height:26px; text-align:center; font-weight:300;">
																												Mettle Super Elite Gainer XXL (Cookies & Cream, 3kg)
																											</td>
																										</tr>
																										<tr>
																											<td class="h4-2 fw-semibold" style="padding-bottom: 20px; color:#979797; font-family:'Poppins', Arial,sans-serif; font-size:20px; line-height:24px; text-align:center; font-weight:600;">
																												<span class="link" style="color:#66b7f0; text-decoration:none;">MRP 3299</span>
																											</td>
																										</tr>
																										<tr>
																											<td align="center">
																												<!-- Button -->
																												<table border="0" cellspacing="0" cellpadding="0">
																													<tr>
																														<td class="text-btn" bgcolor="#ffffff" style="color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:14px; line-height:18px; text-align:center; border:1px solid #e5e5e5; padding:12px 20px;">
																															<a href="https://getmymettle.com/product/mettle-super-elite-gainer-xxl-cookies-and-cream-3kg/" target="_blank" class="link-2" style="color:#4a4a4a; text-decoration:none;"><span class="link-2" style="color:#4a4a4a; text-decoration:none;">SHOP NOW</span></a>
																														</td>
																													</tr>
																												</table>
																												<!-- END Button -->
																											</td>
																										</tr>
																									</table>
																								</td>
																							</tr>
																						</table>
																					</th>
																				</tr>
																			</table>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
													<!-- END 2 Cols -->
												</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - 2 Cols -->
						</td>
					</tr>

					<tr>
						<td>
							<!-- Section - Separator Grey 50px - 2 -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
								<tr>
									<td align="center" valign="top">
										<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td class="img" height="50" style="font-size:0pt; line-height:0pt; text-align:left;">&nbsp;</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Separator Grey 50px - 2 -->
						</td>
					</tr>

					
				</table>
			</td>
		</tr>
	</table>
							<!-- END Section - 4 Cols -->
						</td>
					</tr>
					
					<tr>
						<td>
							<!-- Section - Callout -->
							<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
								<tr>
									<td align="center" valign="top">
										<table width="670" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
											<tr>
												<td style="padding-bottom: 50px;">
													<table width="100%" border="0" cellspacing="0" cellpadding="0">
														<tr>
															<td background="https://getmymettle.com/wp-content/uploads/2020/10/1.jpg" style="-webkit-background-size: cover; background-size: cover;" bgcolor="#4a4a4a" valign="top" height="332" class="m-bg">
																<!--[if gte mso 9]>
																<v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width: 670px; height: 332px;">
																	<v:fill type="frame" src="images/img_68.jpg" color="#4a4a4a" />
																	<v:textbox inset="0,0,0,0">
																<![endif]-->
																<div>
																	<table width="100%" border="0" cellspacing="0" cellpadding="0">
																		<tr>
																			<td class="m-td" width="30" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
																			<td class="h-auto plr-15" height="272" style="padding: 40px 0;">
																				<table width="100%" border="0" cellspacing="0" cellpadding="0" style="background: url(https://getmymettle.com/wp-content/uploads/2020/12/img_1px_transparent_1.png) 0 0 transparent !important;" bgcolor="#ffffff">
																					<tr>
																						<td class="m-td" width="60" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
																						<td class="plr-15" style="padding: 30px 0;">
																							<table width="100%" border="0" cellspacing="0" cellpadding="0">
																								<tr>
																									<td class="h1 fw-medium" style="padding-bottom: 20px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:40px; line-height:50px; text-align:center; font-weight:500;">
																										Download our app
																									</td>
																								</tr>
																								<tr>
																									<td class="text-1" style="padding-bottom: 30px; color:#4a4a4a; font-family:'Poppins', Arial,sans-serif; font-size:16px; line-height:30px; text-align:center;">
																										Get exciting goodies and cashback on every order placed form GetMyMettle android app.
																									</td>
																								</tr>
																								<tr>
																									<td align="center">
																										<!-- Button -->
																										<table border="0" cellspacing="0" cellpadding="0">
																											<tr>
																												<td class="text-btn-large-white" bgcolor="#4a4a4a" style="color:#ffffff; font-family:'Poppins', Arial,sans-serif; font-size:14px; line-height:18px; text-align:center; padding:15px 35px;">
																													<a href="https://play.google.com/store/apps/details?id=com.mettle.getmymettle" target="_blank" class="link-white" style="color:#ffffff; text-decoration:none;"><span class="link-white" style="color:#ffffff; text-decoration:none;">Download Now</span></a>
																												</td>
																											</tr>
																										</table>
																										<!-- END Button -->
																									</td>
																								</tr>
																							</table>
																						</td>
																						<td class="m-td" width="60" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
																					</tr>
																				</table>
																			</td>
																			<td class="m-td" width="30" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
																		</tr>
																	</table>
																</div>
																<!--[if gte mso 9]>
																	</v:textbox>
																</v:rect>
																<![endif]-->
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
							<!-- END Section - Callout -->
						</td>
					</tr>
				</table>
				<!-- END Main -->

				<!-- Footer -->
				<table width="100%" border="0" cellspacing="0" cellpadding="0">
					<tr>
						<td align="center" valign="top">
							<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
								<tr>
									<td class="plr-15" style="padding: 40px 30px;">
										<table width="100%" border="0" cellspacing="0" cellpadding="0">
											<tr>
												<th class="column-top" valign="top" width="225" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
													<div class="img-center" style="font-size:0pt; line-height:0pt; text-align:center;"><a href="#" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/06/logomettle.png" border="0" width="225" height="50" alt="" /></a></div>
												</th>
												<th class="column-top" valign="top" width="15" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"><div style="font-size:0pt; line-height:0pt;" class="m-br-15"></div>
</th>
												<th class="column-top" valign="top" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
													<table width="100%" border="0" cellspacing="0" cellpadding="0">
														<tr>
															<td align="right" style="padding: 15px 0 25px 0;">
																<!-- Socials -->
																<table border="0" cellspacing="0" cellpadding="0" class="center">
																	<tr>
																		<td class="img" width="11" style="font-size:0pt; line-height:0pt; text-align:left;"><a href="https://www.facebook.com/getmymettle" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/12/ico_facebook_light.png" width="11" height="22" border="0" alt="" /></a></td>
																		<td class="img" width="40" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
																		
																		
																		<td class="img" width="22" style="font-size:0pt; line-height:0pt; text-align:left;"><a href="https://www.instagram.com/getmymettle/" target="_blank"><img src="https://getmymettle.com/wp-content/uploads/2020/12/ico_instagram_light.png" width="22" height="22" border="0" alt="" /></a></td>
																		
																	</tr>
																</table>
																<!-- END Socials -->
															</td>
														</tr>
														<tr>
															<td class="text-footer-1 to-right m-center" style="color:#a0a09a; font-family:'Poppins', Arial,sans-serif; font-size:11px; line-height:22px; text-align:right;">
																<span class="link-4" style="color:#a0a09a; text-decoration:none;"> 201/7, 2nd floor, New Vardhman Market\n West Enclave, Pitam Pura\n Delhi-110034</span><br />
																Copyright &copy; Getmymettle
															</td>
														</tr>
													</table>
												</th>
											</tr>
										</table>
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
				<!-- END Footer -->

				<!-- Bottom -->
				<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
					<tr>
						<td align="center" valign="top">
							<table width="650" border="0" cellspacing="0" cellpadding="0" class="mobile-shell">
								<tr>
									<td class="text-bottom" style="padding: 35px 15px; color:#888888; font-family:'Poppins', Arial,sans-serif; font-size:11px; line-height:18px; text-align:center;">
										You are receiving this email because you have subscribed to receive updates from us.<br />
										Should you wish to cancel your subscription, please <a href="https://getmymettle.com/email/?p=unsubscribe" target="_blank" class="link-3-u" style="color:#a8a8a8; text-decoration:underline;"><span class="link-3-u" style="color:#a8a8a8; text-decoration:underline;">click here to unsubscribe.</span></a>
										
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
				<!-- END Bottom -->
			</td>
		</tr>
	</table>
</body>
</html>





            """            

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

file_name = sys.argv[1]

count = 0

with open(file_name,'r') as file:
    emails = file.readlines()
    for email in emails:
        email = email.strip()
        
    # Try to send the email.
        try:
    #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        email,
                        ],
                    },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                            },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                            },
                        },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                        },
                    },
                Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
                Tags=[
                    {
                        'Name': 'Mailer_Analytics',
                        'Value': 'Special40'
                        },
                    ],
                ConfigurationSetName=CONFIGURATION_SET,
                )
            time.sleep(0.05)
# Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            count+=1
            print(count.__str__()+"." ),
            print("Email sent! Message ID:"),
            print(response['MessageId'])