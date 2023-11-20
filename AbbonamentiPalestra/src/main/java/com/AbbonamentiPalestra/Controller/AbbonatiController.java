package com.AbbonamentiPalestra.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Service.AbbonatiService;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/abbonati")
public class AbbonatiController {

	@Autowired private AbbonatiService abbonatiService;
	
	
	
}
