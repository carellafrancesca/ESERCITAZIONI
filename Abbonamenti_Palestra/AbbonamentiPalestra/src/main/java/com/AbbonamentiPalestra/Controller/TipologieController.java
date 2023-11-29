package com.AbbonamentiPalestra.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/tipi")
public class TipologieController {
	
	 @GetMapping("/attivita")
	 public TipoAttivita[] getTipiAttivita() {
	      return TipoAttivita.values();
	 }

	 @GetMapping("/abbonamento")
	 public TipoAbbonamento[] getTipiAbbonamento() {
	      return TipoAbbonamento.values();
	 }
	
}
