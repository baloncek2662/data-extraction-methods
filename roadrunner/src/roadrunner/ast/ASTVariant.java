/*
     RoadRunner - an automatic wrapper generation system for Web data sources
     Copyright (C) 2003  Valter Crescenzi - crescenz@dia.uniroma3.it

     This program is  free software;  you can  redistribute it and/or
     modify it  under the terms  of the GNU General Public License as
     published by  the Free Software Foundation;  either version 2 of
     the License, or (at your option) any later version.

     This program is distributed in the hope that it  will be useful,
     but  WITHOUT ANY WARRANTY;  without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
     General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with this program; if not, write to the:

     Free Software Foundation, Inc.,
     59 Temple Place, Suite 330,
     Boston, MA 02111-1307 USA

     ----

     RoadRunner - un sistema per la generazione automatica di wrapper su sorgenti Web
     Copyright (C) 2003  Valter Crescenzi - crescenz@dia.uniroma3.it

     Questo  programma    software libero;    lecito redistribuirlo  o
     modificarlo secondo i termini della Licenza Pubblica Generica GNU
     come   pubblicata dalla Free Software Foundation; o la versione 2
     della licenza o (a propria scelta) una versione successiva.

     Questo programma    distribuito nella speranza che sia  utile, ma
     SENZA  ALCUNA GARANZIA;  senza neppure la  garanzia implicita  di
     NEGOZIABILIT   o di  APPLICABILIT  PER  UN PARTICOLARE  SCOPO. Si
     veda la Licenza Pubblica Generica GNU per avere maggiori dettagli.

     Questo  programma deve  essere  distribuito assieme  ad una copia
     della Licenza Pubblica Generica GNU; in caso contrario, se ne pu
     ottenere  una scrivendo  alla:

     Free  Software Foundation, Inc.,
     59 Temple Place, Suite 330,
     Boston, MA 02111-1307 USA

*/
/**
 * ASTVariant.java
 * Created: 
 *
 * @author  Valter Crescenzi
 * @version
 */
package roadrunner.ast;

import java.util.*;

import roadrunner.parser.Token;

public class ASTVariant extends NodeAdapter implements Node, Matchable {
    
    private List samples;
    private String label;
    
    private Token sampleToken;
    
    ASTVariant(Token token) {
        super(ASTConstants.JJTVARIANT);
        this.sampleToken = token;
        this.samples = new ArrayList();
        this.label = null;
    }
    
    /** Accept the visitor. **/
    public boolean jjtAccept(Visitor visitor) {
        return visitor.visit(this);
    }
    
    public Token getToken() {
        return this.sampleToken;
    }
    
    public boolean matches(Token t) {
        return this.getToken().matches(t);
    }
    
    public int depth() {
        return getToken().depth();
    }
    
    public int code() {
        return getToken().code();
    }
    public void setLabel(String label) {
        this.label = label;
    }
    
    public String getLabel() {
        return this.label;
    }
    
    public void setSamples(Set strings) {
        this.samples.addAll(strings);
    }
    
    public List getSamples() {
        return this.samples;
    }
    
    public String toString() {
        List samples = getSamples();
        Object sample = (!samples.isEmpty() ? (Object)samples : getToken() );
        return "*" + " ( "+getLabel()+" ) " + sample;
    }
    
    public boolean equals(Object o) {
        if (!super.equals(o)) return false;
        ASTVariant that = (ASTVariant)o;
        return this.getToken().code()==that.getToken().code() && 
               this.getToken().depth()==that.getToken().depth();
    }
    
    public int hashCode() {
        return this.getToken().hashCode();
    }
    
    
}
